from pygame import *

window = display.set_mode((960, 520))
clock = time.Clock()
game = True

lost_label = pygame.font.SysFont('arial', 25).render('TEST', True, (255,255,255))

while game:
  for i in event.get():
    if i.type == QUIT:
      game = False
    window.fill((125, 125, 0))
    lost_label.blit()
    display.update()
    clock.tick(60)
