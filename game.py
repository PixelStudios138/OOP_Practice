import pygame
import sys

# --- Constants ---
WIDTH, HEIGHT = 800, 600
INVADER_SIZE = 40
COLUMNS, ROWS = 10, 5
INVADER_GAP = 10
SPEED = 2

# --- Invader Class ---
class Invader:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = INVADER_SIZE
        self.alive = True

    def draw(self, surface):
        if self.alive:
            pygame.draw.rect(surface, (0, 255, 0), (self.x, self.y, self.size, self.size))

    def rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

# --- Setup ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders Demo")
clock = pygame.time.Clock()

# --- Create Matrix of Invaders ---
invaders = []
start_x = (WIDTH - (COLUMNS * INVADER_SIZE + (COLUMNS - 1) * INVADER_GAP)) // 2
start_y = 50
for row in range(ROWS):
    for col in range(COLUMNS):
        x = start_x + col * (INVADER_SIZE + INVADER_GAP)
        y = start_y + row * (INVADER_SIZE + INVADER_GAP)
        invaders.append(Invader(x, y))

# --- Movement Variables ---
direction = 1  # 1 = right, -1 = left
move_down = False

# --- Main Loop ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            # Check if any invader is clicked
            for invader in invaders:
                if invader.alive and invader.rect().collidepoint(mx, my):
                    invader.alive = False  # Remove invader

    # --- Move Invaders ---
    # Find edges
    leftmost = min([inv.x for inv in invaders if inv.alive], default=0)
    rightmost = max([inv.x + inv.size for inv in invaders if inv.alive], default=WIDTH)
    # Change direction if at edge
    if direction == 1 and rightmost + SPEED > WIDTH:
        direction = -1
        move_down = True
    elif direction == -1 and leftmost - SPEED < 0:
        direction = 1
        move_down = True
    # Move all invaders
    for invader in invaders:
        if invader.alive:
            invader.x += SPEED * direction
            if move_down:
                invader.y += INVADER_SIZE // 2
    move_down = False

    # --- Draw ---
    screen.fill((0, 0, 0))
    for invader in invaders:
        invader.draw(screen)
    # --- Explainer text ---
    font = pygame.font.SysFont(None, 28)
    text = font.render("Click a green square to remove it!", True, (255,255,255))
    screen.blit(text, (20, HEIGHT - 40))
    pygame.display.flip()
    clock.tick(60)
