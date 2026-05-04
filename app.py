import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Yes Yes App")
clock = pygame.time.Clock()

# Font
font_large = pygame.font.Font(None, 48)
font_small = pygame.font.Font(None, 36)

# States
STATE_START = 0
STATE_GAME = 1
STATE_END = 2

current_state = STATE_START

# Button class
class Button:
    def __init__(self, x, y, width, height, text, color, text_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.text_color = text_color
        self.is_circle = False
    
    def draw(self, surface):
        if self.is_circle:
            pygame.draw.circle(surface, self.color, self.rect.center, self.rect.width // 2)
        else:
            pygame.draw.rect(surface, self.color, self.rect)
        
        text_surf = font_small.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)
    
    def is_clicked(self, pos):
        if self.is_circle:
            dx = pos[0] - self.rect.centerx
            dy = pos[1] - self.rect.centery
            distance = (dx**2 + dy**2)**0.5
            return distance <= self.rect.width // 2
        else:
            return self.rect.collidepoint(pos)

# Create buttons
start_button = Button(WIDTH // 2 - 100, HEIGHT // 2 - 30, 200, 60, "Click To Start", WHITE, BLACK)
game_button = Button(WIDTH // 2, HEIGHT // 2, 100, 100, "Start", RED, BLACK)
game_button.is_circle = True

end_button = Button(WIDTH // 2 - 75, HEIGHT // 2 - 30, 150, 60, "OK BYE", WHITE, BLACK)

# Main loop
running = True
while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            
            if current_state == STATE_START:
                if start_button.is_clicked(mouse_pos):
                    current_state = STATE_GAME
            
            elif current_state == STATE_GAME:
                if game_button.is_clicked(mouse_pos):
                    current_state = STATE_END
            
            elif current_state == STATE_END:
                if end_button.is_clicked(mouse_pos):
                    current_state = STATE_START
    
    # Draw
    if current_state == STATE_START:
        screen.fill(WHITE)
        start_button.draw(screen)
    
    elif current_state == STATE_GAME:
        screen.fill(BLACK)
        game_button.draw(screen)
    
    elif current_state == STATE_END:
        screen.fill(WHITE)
        end_text = font_large.render("OK BYE", True, BLACK)
        text_rect = end_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(end_text, text_rect)
        end_button.draw(screen)
    
    pygame.display.flip()

pygame.quit()
sys.exit()
