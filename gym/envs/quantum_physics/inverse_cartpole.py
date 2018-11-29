"""
Created on Wed Okt 24
@authors: katja, lea

The following new gym classic_control environment is a modified copy of the cartpole problem in the OpenAI Gym github repository as of 2018-09-26.
"""

"""
Classic cart-pole system implemented by Rich Sutton et al.
Copied from http://incompleteideas.net/sutton/book/code/pole.c
permalink: https://perma.cc/C9ZM-652R

"""

import math
import gym
from gym import spaces, logger
from gym.utils import seeding
import numpy as np

class InverseCartPoleEnv(gym.Env):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second' : 50
    }

    def __init__(self):
        self.gravity = 9.8
        self.masscart = 1.0
        self.masspole = 0.1
        self.total_mass = (self.masspole + self.masscart)
        self.length = 0.5 # actually half the pole's length
        self.polemass_length = (self.masspole * self.length)
        self.force_mag = 10.0
        self.tau = 0.02  # seconds between state updates
        self.max_steps_per_trial = 1000
        self.step_counter = 0
        # Conditions to fail the episode
        #self.theta_threshold_radians = 12 * 2 * math.pi / 360
        #self.x_threshold = 2.4
        self.max_theta = np.pi
        self.world_width = 6
        self.x_goal = 1 
        self.x_start = -2
        self.change = self.max_steps_per_trial

        # theta limit set to 2 * theta_threshold_radians so failing observation is still within bounds
        high = np.array([
            self.world_width,
            np.finfo(np.float32).max,
            self.max_theta * 2,
            np.finfo(np.float32).max])

        self.action_space = spaces.Box(low=np.array([-10.0,-1.0]), high=np.array([10.0,1.0]), dtype=np.float32)
        self.observation_space = spaces.Box(-high, high, dtype=np.float32)

        self.seed()
        self.viewer = None
        self.state = None

        self.steps_beyond_done = None

    def parameter_settings(self, world_width, max_steps, goal):
        self.world_width = world_width
        self.max_steps_per_trial = max_steps
        self.goal = goal

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]


    def step(self, action):
        self.step_counter += 1
        assert self.action_space.contains(action), "%r (%s) invalid"%(action, type(action))
        act_accel, act_length = action 
        state = self.state
        x, x_dot, theta, theta_dot = state
        force = act_accel*self.force_mag 
        #force = self.force_mag if action==1 else -self.force_mag
        costheta = math.cos(theta)
        sintheta = math.sin(theta)
        temp = (force + self.polemass_length * theta_dot * theta_dot * sintheta) / self.total_mass
        thetaacc = (self.gravity * sintheta - costheta* temp) / (self.length * (4.0/3.0 - self.masspole * costheta * costheta / self.total_mass))
        xacc  = temp - self.polemass_length * thetaacc * costheta / self.total_mass
        x  = x + self.tau * x_dot
        x_dot = x_dot + self.tau * xacc
        theta = theta + self.tau * theta_dot
        theta_dot = theta_dot + self.tau * thetaacc
        self.state = (x,x_dot,theta,theta_dot)
        done = x < -self.world_width/2 or x > self.world_width/2
        if self.step_counter == self.max_steps_per_trial-1:
            self.step_counter = 0 #changed that, might not be necessary
            done = True


        #REWARD:

        #if self.step_counter > self.change:
        #    reward = self.reward_pos()
        #else:
        reward = self.reward_posandpole()

                #x < -self.x_threshold \
                #or x > self.x_threshold \
                #or theta < -self.theta_threshold_radians \
                #or theta > self.theta_threshold_radians
        done = bool(done)

        #if not done:
        #    reward = 0.0
        #elif self.steps_beyond_done is None:
            # Pole just fell!
        #    self.steps_beyond_done = 0
        #    reward = 1.0
        #else:
        #    if self.steps_beyond_done == 0:
        #        logger.warn("You are calling 'step()' even though this environment has already returned done = True. You should always call 'reset()' once you receive 'done = True' -- any further steps are undefined behavior.")
        #    self.steps_beyond_done += 1
        #    reward = 0.0
        

        return np.array(self.state), reward, done, {}
    
    def energy_pole(self):
        """returns the energy in the pole (kinetic and potential)"""
        #recall that self.length is half the actual length of the pole
        potential = self.gravity*self.polemass_length*(np.cos(self.state[2]) +1)
        kinetic = 2*self.masspole*self.length*(self.state[3]**2)
        return potential+kinetic

    def energy_cart(self):
        """returns the kinetic energy of the cart"""
        kinetic = 1/2*self.masscart*(self.state[2]**2)
        return kinetic

    def reward_posandpoleandcart(self):
        """Returns a reward for (a) getting close to a target position in x,
        (b) keeping the energy of the pole low, and (c) keeping energy of cart low. All three functions are continuous-valued and vary rather smoothly."""
        goal = np.exp(-4*(self.state[0] - self.x_goal)**2)
        return(goal*np.exp(-self.energy_pole()*2)*np.exp(-self.energy_cart()*2))

    def reward_posandpole(self):
        """Returns a reward for (a) getting close to a target position in x and
        (b) keeping the energy of the pole low. Both functions are continuous-valued and vary rather smoothly."""
        goal = np.exp(-4*(self.state[0] - self.x_goal)**2)
        return(goal*np.exp(-self.energy_pole()*2))

    
    def reward_pos(self):
        """Returns reward for getting close to a target position in x.
          The function is continuous-valued and varies rather smoothly."""
        goal = np.exp(-4*(self.state[0] - self.x_goal)**2)
        return goal

    def reward_pole(self):
        return (goal * np.exp(-self.energy_pole() * 2) * np.exp(-self.energy_cart() * 2))


    def reward_posandpoleandcart(self):
        pass


     
    def reset(self):
        self.state = self.np_random.uniform(low=-0.05, high=0.05, size=(4,))
        self.state[2] += math.pi #initialize pole theta to be (approx) straight down
        self.state[0] += self.x_start #start at/near x_start
        self.steps_beyond_done = None
        self.step_counter = 0
        return np.array(self.state)

    def render(self, mode='human'):
        """This raises a NotImplementedError('abstract') error in get_screens.
        Solution: downgrade to pyglet 1.2.4
        maybe an alternative solution: env.close() at the end of the run file
        """
        screen_width = 600
        screen_height = 400
        scale = screen_width/self.world_width
        goal_position = screen_width/2+self.x_goal*scale
        carty = 200 # TOP OF CART
        polewidth = 10.0
        polelen = scale * 1.0
        cartwidth = 50.0
        cartheight = 30.0

        if self.viewer is None: 
            #if the viewer is currently off, initialize a bunch of elements
            from gym.envs.classic_control import rendering
            self.viewer = rendering.Viewer(screen_width, screen_height)
            l,r,t,b = -cartwidth/2, cartwidth/2, cartheight/2, -cartheight/2
            axleoffset =cartheight/4.0
            cart = rendering.FilledPolygon([(l,b), (l,t), (r,t), (r,b)])
            self.carttrans = rendering.Transform()
            cart.add_attr(self.carttrans)
            self.viewer.add_geom(cart)
            l,r,t,b = -polewidth/2,polewidth/2,polelen-polewidth/2,-polewidth/2
            pole = rendering.FilledPolygon([(l,b), (l,t), (r,t), (r,b)])
            pole.set_color(.8,.6,.4)
            self.poletrans = rendering.Transform(translation=(0, axleoffset))
            pole.add_attr(self.poletrans)
            pole.add_attr(self.carttrans)
            self.viewer.add_geom(pole)
            self.axle = rendering.make_circle(polewidth/2)
            self.axle.add_attr(self.poletrans)
            self.axle.add_attr(self.carttrans)
            self.axle.set_color(.5,.5,.8)
            self.viewer.add_geom(self.axle)
            self.track = rendering.Line((0,carty), (screen_width,carty))
            self.track.set_color(0,0,0)
            self.viewer.add_geom(self.track)
            self.goal = rendering.Line((goal_position,0),(goal_position,screen_height))
            self.goal.set_color(0,0,0)
            self.viewer.add_geom(self.goal)
                        
            self.energybar = self.add_display(20,(1,0,0))
            #self.lengthbar = self.add_display(100,(0,0,0))
            self.rewardbar = self.add_display(60,(0,1,0))
            
        if self.state is None: return None

        #now that the viewer is on, apply updated transformations to move elements dynamically
        x = self.state
        cartx = x[0]*scale+screen_width/2.0 # MIDDLE OF CART
        self.carttrans.set_translation(cartx, carty)
        self.poletrans.set_rotation(-x[2])
        #move display bars in the y direction to reflect the values of the corresponding functions
        self.energybar.attrs[1].set_translation(0,30*self.energy_pole()) #display kinetic and potential energy of the pole
        #self.lengthbar.attrs[1].set_translation(0,10*(self.length-self.min_length)) #display how the agent changes the length of the pole
        self.rewardbar.attrs[1].set_translation(0,100*self.reward_pos())

        return self.viewer.render(return_rgb_array = mode=='rgb_array')

    def add_display(self, posx, rgb):
        """Within render, add a column for displaying some scalar variable."""
        from gym.envs.classic_control import rendering
        l,r,t,b = posx-10, posx+10, 195, 205
        valuebar = rendering.FilledPolygon([(l,b), (l,t), (r,t), (r,b)])
        for offset in [0,50,100,150]:
            refbar = rendering.Line((l,offset+200), (r, offset+200))
            refbar.set_color(0.5,0.5,0.5)
            self.viewer.add_geom(refbar)
        valuebar.set_color(rgb[0],rgb[1],rgb[2])
        valuebar_trans = rendering.Transform(translation = (0,0))
        valuebar.add_attr(valuebar_trans)
        self.viewer.add_geom(valuebar)
        return valuebar

    def close(self):
        if self.viewer: self.viewer.close()
