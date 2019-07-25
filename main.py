import pygame
from car import Car
from bird import Bird
from background import Background
from pipe import Pipe
from flor import Flor
from game import Game

carryOn = True
game = Game(game_width=288,game_height=512,pipe_distance=200)
while carryOn:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game.bird.stopped:
                    game.start()
                game.bird.jump()

    game.move_pipes()
    collided = game.bird.is_collided_with(game.game_objects)
    if collided:
        game.reset()

    game.update_middle_sprites()
    game.count_score()
    game.fill_game_screen()

    game.draw_middle_sprites()
    game.draw_front_sprites()

    game.render_score()

    pygame.display.flip()
    game.tick(60)

pygame.quit()

    






