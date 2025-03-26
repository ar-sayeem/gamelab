import pygame
import random
import numpy as np  # <-- Add this import

# Fireworks/Sparks particles class
class Particle:
    def __init__(self, x, y, color, radius):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.angle = random.uniform(0, 2 * np.pi)
        self.speed = random.uniform(1, 4)
        self.lifetime = random.randint(20, 50)  # Number of frames to live
    
    def update(self):
        self.x += self.speed * np.cos(self.angle)
        self.y += self.speed * np.sin(self.angle)
        self.lifetime -= 1
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# Function to create fireworks effect
def create_fireworks(x, y, CIRCLE_COLOR, CROSS_COLOR):
    particles = []
    for _ in range(50):  # Number of particles
        color = random.choice([CIRCLE_COLOR, CROSS_COLOR, (255, 255, 0)])  # Red, Green, Yellow
        radius = random.randint(2, 6)
        particles.append(Particle(x, y, color, radius))
    return particles

# Function to display fireworks
def display_fireworks(screen, x, y, CIRCLE_COLOR, CROSS_COLOR):
    particles = create_fireworks(x, y, CIRCLE_COLOR, CROSS_COLOR)
    for particle in particles:
        particle.update()
        particle.draw(screen)
