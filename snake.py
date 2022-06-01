import pygame
from time import sleep
from random import randint

pygame.init()
screen = pygame.display.set_mode((601,640))
pygame.display.set_caption("Snake")

running = True

GREEN = (0,200,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
YELLOW = (255,255,0)
ORANGE = (255,165,0)
BROWN = (165,45,45)
clock = pygame.time.Clock()

snake = [[2,9], [3,9], [4,9]]
wall = []
direction = "right"
speed = 0
font = pygame.font.SysFont('sans',20)
status = "menu"
first_apple = True
direction_change = False
score = 0
previous_tail_x = 2
previous_tail_y = 9
previous_direction = "right"

apple_image = pygame.image.load("apple.png")
apple_image = pygame.transform.scale(apple_image, (30,30))


while running:
	clock.tick(60)
	screen.fill(BLACK)


	if status == "menu":
		pygame.draw.rect(screen, WHITE, (200, 100, 200, 315))

		select_mode_txt = font.render("Select Mode", True, BLACK)
		screen.blit(select_mode_txt, (252, 113))

		pygame.draw.rect(screen, GREEN, (225, 150, 150, 50))
		no_wall_txt = font.render("NO WALL", True, BLACK)
		screen.blit(no_wall_txt, (262, 162))

		pygame.draw.rect(screen, YELLOW, (225, 215, 150, 50))
		box_txt = font.render("BOX", True, BLACK)
		screen.blit(box_txt, (280, 227))

		pygame.draw.rect(screen, ORANGE, (225, 280, 150, 50))
		railway_txt = font.render("RAILWAY", True, BLACK)
		screen.blit(railway_txt, (263, 292))

		pygame.draw.rect(screen, RED, (225, 345, 150, 50))
		house_txt = font.render("HOUSE", True, BLACK)
		screen.blit(house_txt, (270, 357))



	elif status == "speed select":
		pygame.draw.rect(screen, WHITE, (225, 100, 150, 400))

		select_speed_txt = font.render("Select Speed", True, BLACK)
		screen.blit(select_speed_txt, (250, 113))

		for i in range(8):
			pygame.draw.rect(screen, ORANGE, (250, 150 + i*42, 100, 35))
			speed_txt = font.render(str(i+1), True, BLACK)
			screen.blit(speed_txt, (295, 156 + i*42))

		pygame.draw.rect(screen, WHITE, (30, 30, 61, 30))
		back_txt = font.render("Back", True, BLACK)
		screen.blit(back_txt, (42,32))



	elif status == "play":

		if first_apple:
			apple = [randint(0,19), randint(0,19)]
			while (apple in snake) or (apple in wall):
				apple = [randint(0,19), randint(0,19)]
			first_apple = False

		tail_x = snake[0][0]
		tail_y = snake[0][1]


		#draw apple
		screen.blit(apple_image, (apple[0]*30, apple[1]*30))

		#draw snake
		for part in snake:
			if part == snake[0]: #tail
				if snake[0][0] == snake[1][0] - 1:
					pygame.draw.polygon(screen, GREEN, [((part[0]+1)*30, part[1]*30), ((part[0]+1)*30, (part[1]+1)*30), (part[0]*30, part[1]*30 + 15)])
				if snake[0][0] == snake[1][0] + 1:
					pygame.draw.polygon(screen, GREEN, [(part[0]*30, part[1]*30), (part[0]*30, (part[1]+1)*30), ((part[0]+1)*30, part[1]*30 + 15)])
				if snake[0][1] == snake[1][1] + 1:
					pygame.draw.polygon(screen, GREEN, [(part[0]*30, part[1]*30), ((part[0]+1)*30, part[1]*30), (part[0]*30 + 15, (part[1]+1)*30)])
				if snake[0][1] == snake[1][1] - 1:
					pygame.draw.polygon(screen, GREEN, [(part[0]*30, (part[1]+1)*30), ((part[0]+1)*30, (part[1]+1)*30), (part[0]*30 + 15, part[1]*30)])
			elif part == snake[-1]: #head
				if direction == "right":
					pygame.draw.polygon(screen, GREEN, [(part[0]*30, part[1]*30), (part[0]*30, (part[1]+1)*30), (part[0]*30 + 15, (part[1]+1)*30), ((part[0]+1)*30, part[1]*30 + 20), ((part[0]+1)*30, part[1]*30 + 10), (part[0]*30 + 15, part[1]*30)])
				if direction == "left":
					pygame.draw.polygon(screen, GREEN, [((part[0]+1)*30, part[1]*30), ((part[0]+1)*30, (part[1]+1)*30), (part[0]*30 + 15, (part[1]+1)*30), (part[0]*30, part[1]*30 + 20), (part[0]*30, part[1]*30 + 10), (part[0]*30 + 15, part[1]*30)])
				if direction == "up":
					pygame.draw.polygon(screen, GREEN, [(part[0]*30, (part[1]+1)*30), ((part[0]+1)*30, (part[1]+1)*30), ((part[0]+1)*30, part[1]*30 + 15), (part[0]*30 + 20, part[1]*30), (part[0]*30 + 10, part[1]*30), (part[0]*30, part[1]*30 + 15)])
				if direction == "down":
					pygame.draw.polygon(screen, GREEN, [(part[0]*30, part[1]*30), ((part[0]+1)*30, part[1]*30), ((part[0]+1)*30, part[1]*30 + 15), (part[0]*30 + 20, (part[1]+1)*30), (part[0]*30 + 10, (part[1]+1)*30), (part[0]*30, part[1]*30 + 15)])
			else:
				pygame.draw.rect(screen, GREEN, (part[0]*30, part[1]*30, 30, 30))
		#eyes
		if direction == "right" or direction == "left":
			pygame.draw.circle(screen, WHITE, (snake[-1][0]*30 + 15, snake[-1][1]*30 + 7), 2)
			pygame.draw.circle(screen, WHITE, (snake[-1][0]*30 + 15, snake[-1][1]*30 + 23), 2)
		if direction == "up" or direction == "down":
			pygame.draw.circle(screen, WHITE, (snake[-1][0]*30 + 7, snake[-1][1]*30 + 15), 2)
			pygame.draw.circle(screen, WHITE, (snake[-1][0]*30 + 23, snake[-1][1]*30 + 15), 2)

		#draw wall
		for part in wall:
			pygame.draw.rect(screen, BROWN, (part[0]*30, part[1]*30, 30, 30))

		#draw border
		pygame.draw.line(screen, WHITE, (0,0), (0,600))
		pygame.draw.line(screen, WHITE, (0,0), (600,0))
		pygame.draw.line(screen, WHITE, (600,0), (600,600))
		pygame.draw.line(screen, WHITE, (0,600), (600,600))

		#write score
		score_txt = font.render("Score: " + str(score), True, WHITE)
		screen.blit(score_txt, (5,607))

		pygame.draw.rect(screen, WHITE, (535, 605, 61, 30))
		menu_txt = font.render("Menu", True, BLACK)
		screen.blit(menu_txt, (545,607))

		#eat apple
		if snake[-1] == apple:
			score += 1
			snake.insert(0,[tail_x, tail_y])

			#generate apple
			apple = [randint(0,19), randint(0,19)]
			while (apple in snake) or (apple in wall):
				apple = [randint(0,19), randint(0,19)]			

		#losing
		if (snake[-1] in wall) or (snake[-1] in snake[:-1]):
			status = "lose"
			snake.insert(0, [previous_tail_x, previous_tail_y])
			snake.pop(-1)

		sleep(speed)

		

	elif status == "lose":

		for part in snake:
			if part == snake[0]: 
				if snake[0][0] == snake[1][0] - 1:
					pygame.draw.polygon(screen, GREEN, [((part[0]+1)*30, part[1]*30), ((part[0]+1)*30, (part[1]+1)*30), (part[0]*30, part[1]*30 + 15)])
				if snake[0][0] == snake[1][0] + 1:
					pygame.draw.polygon(screen, GREEN, [(part[0]*30, part[1]*30), (part[0]*30, (part[1]+1)*30), ((part[0]+1)*30, part[1]*30 + 15)])
				if snake[0][1] == snake[1][1] + 1:
					pygame.draw.polygon(screen, GREEN, [(part[0]*30, part[1]*30), ((part[0]+1)*30, part[1]*30), (part[0]*30 + 15, (part[1]+1)*30)])
				if snake[0][1] == snake[1][1] - 1:
					pygame.draw.polygon(screen, GREEN, [(part[0]*30, (part[1]+1)*30), ((part[0]+1)*30, (part[1]+1)*30), (part[0]*30 + 15, part[1]*30)])
			elif part == snake[-1]: 
				if previous_direction == "right":
					pygame.draw.polygon(screen, GREEN, [(part[0]*30, part[1]*30), (part[0]*30, (part[1]+1)*30), (part[0]*30 + 15, (part[1]+1)*30), ((part[0]+1)*30, part[1]*30 + 20), ((part[0]+1)*30, part[1]*30 + 10), (part[0]*30 + 15, part[1]*30)])
				if previous_direction == "left":
					pygame.draw.polygon(screen, GREEN, [((part[0]+1)*30, part[1]*30), ((part[0]+1)*30, (part[1]+1)*30), (part[0]*30 + 15, (part[1]+1)*30), (part[0]*30, part[1]*30 + 20), (part[0]*30, part[1]*30 + 10), (part[0]*30 + 15, part[1]*30)])
				if previous_direction == "up":
					pygame.draw.polygon(screen, GREEN, [(part[0]*30, (part[1]+1)*30), ((part[0]+1)*30, (part[1]+1)*30), ((part[0]+1)*30, part[1]*30 + 15), (part[0]*30 + 20, part[1]*30), (part[0]*30 + 10, part[1]*30), (part[0]*30, part[1]*30 + 15)])
				if previous_direction == "down":
					pygame.draw.polygon(screen, GREEN, [(part[0]*30, part[1]*30), ((part[0]+1)*30, part[1]*30), ((part[0]+1)*30, part[1]*30 + 15), (part[0]*30 + 20, (part[1]+1)*30), (part[0]*30 + 10, (part[1]+1)*30), (part[0]*30, part[1]*30 + 15)])
			else:
				pygame.draw.rect(screen, GREEN, (part[0]*30, part[1]*30, 30, 30))
		for part in wall:
			pygame.draw.rect(screen, BROWN, (part[0]*30, part[1]*30, 30, 30))
		screen.blit(apple_image, (apple[0]*30, apple[1]*30))
		pygame.draw.line(screen, WHITE, (0,0), (0,600))
		pygame.draw.line(screen, WHITE, (0,0), (600,0))
		pygame.draw.line(screen, WHITE, (600,0), (600,600))
		pygame.draw.line(screen, WHITE, (0,600), (600,600))
		if previous_direction == "right" or previous_direction == "left":
			pygame.draw.circle(screen, WHITE, (snake[-1][0]*30 + 15, snake[-1][1]*30 + 7), 2)
			pygame.draw.circle(screen, WHITE, (snake[-1][0]*30 + 15, snake[-1][1]*30 + 23), 2)
		if previous_direction == "up" or previous_direction == "down":
			pygame.draw.circle(screen, WHITE, (snake[-1][0]*30 + 7, snake[-1][1]*30 + 15), 2)
			pygame.draw.circle(screen, WHITE, (snake[-1][0]*30 + 23, snake[-1][1]*30 + 15), 2)


		game_over_txt = font.render("Game Over",True,BLACK)
		pygame.draw.rect(screen, WHITE, (200,200,200,200))
		pygame.draw.rect(screen, RED, (200, 200, 200, 35))
		screen.blit(game_over_txt,(257,205))

		score_txt = font.render("Score: " + str(score), True, BLACK)
		if score < 10:
			screen.blit(score_txt, (268, 237))
		else:
			screen.blit(score_txt, (265, 237))

		restart_txt = font.render("RESTART", True, BLACK)
		pygame.draw.rect(screen, YELLOW, (225,268,150,50))
		screen.blit(restart_txt, (264, 281))

		menu_txt = font.render("MENU", True, BLACK)
		pygame.draw.rect(screen, ORANGE,(225, 333, 150, 50))
		screen.blit(menu_txt, (276, 346))


	mouse_x, mouse_y = pygame.mouse.get_pos()

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if status == "play":
				if event.key == pygame.K_UP and direction != "down":
					if direction_change == False:
						previous_direction = direction
						previous_tail_x = snake[0][0]
						previous_tail_y = snake[0][1]
						direction_change = True
						direction = "up"
						if snake[-1][1] == 0:
							snake.append([snake[-1][0], 19])
						else:
							snake.append([snake[-1][0], snake[-1][1] - 1])
						snake.pop(0)

				if event.key == pygame.K_DOWN and direction != "up":
					if direction_change == False:
						previous_direction = direction
						previous_tail_x = snake[0][0]
						previous_tail_y = snake[0][1]
						direction_change = True
						direction = "down"
						if snake[-1][1] == 19:
							snake.append([snake[-1][0], 0])
						else:
							snake.append([snake[-1][0], snake[-1][1] + 1])
						snake.pop(0)

				if event.key == pygame.K_LEFT and direction != "right":
					if direction_change == False:
						previous_direction = direction
						previous_tail_x = snake[0][0]
						previous_tail_y = snake[0][1]
						direction_change = True
						direction = "left"
						if snake[-1][0] == 0:
							snake.append([19, snake[-1][1]])
						else:
							snake.append([snake[-1][0] - 1, snake[-1][1]])
						snake.pop(0)

				if event.key == pygame.K_RIGHT and direction != "left":
					if direction_change == False:
						previous_direction = direction
						previous_tail_x = snake[0][0]
						previous_tail_y = snake[0][1]
						direction_change = True
						direction = "right"
						if snake[-1][0] == 19:
							snake.append([0, snake[-1][1]])
						else:
							snake.append([snake[-1][0] + 1, snake[-1][1]])
						snake.pop(0)
					


		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:

				if status == "menu":
					if 225 < mouse_x < 375:

						#no wall
						if 150 < mouse_y < 200:
							status = "speed select"


						#box
						if 215 < mouse_y < 265:
							for i in range(20):
								wall.append([i,0])
								wall.append([i,19])
							for i in range(1,19):
								wall.append([0,i])
								wall.append([19,i])
							status = "speed select"


						#railway
						if 280 < mouse_y < 330:
							for i in range(20):
								wall.append([i,0])
								wall.append([i,19])
							for i in range(1,8):
								wall.append([0,i])
								wall.append([19,i])
								wall.append([0,19-i])
								wall.append([19,19-i])
							for i in range(5,15):
								wall.append([i,7])
								wall.append([i,12])
							status = "speed select"


						#house
						if 345 < mouse_y < 395:
							for i in range(8):
								wall.append([i,7])
								wall.append([i,12])
								wall.append([19-i,7])
								wall.append([19-i,12])
								wall.append([7,i])
								wall.append([12,19-i])
							for i in range(2,7):
								wall.append([12,i])
								wall.append([7,19-i])
							for i in range(15,18):
								wall.append([i,2])
								wall.append([i,4])
							for i in range(16,20):
								wall.append([i,15])
							wall.append([19,16])
							wall.append([19,17])
							wall.append([16,18])
							wall.append([16,19])
							wall.append([2,2])
							wall.append([3,2])
							wall.append([3,3])
							for i in range(2,5):
								wall.append([i,16])
							wall.append([3,15])
							wall.append([3,17])
							status = "speed select"


				elif status == "speed select":
					for i in range(8):
						if 250 < mouse_x < 350 and 150 + i*42 < mouse_y < 185 + i*42:
							speed = round(0.1 + 0.05*(7-i), 2)
							status = "play"

					#back to menu
					if 30 < mouse_x < 91 and 30 < mouse_y < 60:
						wall = []
						status = "menu"


				elif status == "play":

					#back to menu
					if 535 < mouse_x < 596 and 605 < mouse_y < 635:
						snake = [[2,9], [3,9], [4,9]]
						wall = []
						direction = "right"
						first_apple = True
						direction_change = False
						score = 0
						status = "menu"
						previous_tail_x = 2
						previous_tail_y = 9
						previous_direction = "right"

				

				elif status == "lose":

					#restart
					if 225 < mouse_x < 375 and 268 < mouse_y < 318:
						snake = [[2,9], [3,9], [4,9]]
						direction = "right"
						first_apple = True
						direction_change = False
						score = 0
						status = "play"
						previous_tail_x = 2
						previous_tail_y = 9
						previous_direction = "right"

					#back to menu
					if 225 < mouse_x < 375 and 333 < mouse_y < 383:
						snake = [[2,9], [3,9], [4,9]]
						wall = []
						direction = "right"
						first_apple = True
						direction_change = False
						score = 0
						status = "menu"
						previous_tail_x = 2
						previous_tail_y = 9
						previous_direction = "right"



	#snake move
	if status == "play":
		if direction_change == False:
			previous_direction = direction
			previous_tail_x = snake[0][0]
			previous_tail_y = snake[0][1]
			if direction == "right":
				if snake[-1][0] == 19:
					snake.append([0, snake[-1][1]])
				else:
					snake.append([snake[-1][0] + 1, snake[-1][1]])
				snake.pop(0)
					
			if direction == "left":
				if snake[-1][0] == 0:
					snake.append([19, snake[-1][1]])
				else:
					snake.append([snake[-1][0] - 1, snake[-1][1]])
				snake.pop(0)
					
			if direction == "up":
				if snake[-1][1] == 0:
					snake.append([snake[-1][0], 19])
				else:
					snake.append([snake[-1][0], snake[-1][1] - 1])
				snake.pop(0)
					
			if direction == "down":
				if snake[-1][1] == 19:
					snake.append([snake[-1][0], 0])
				else:
					snake.append([snake[-1][0], snake[-1][1] + 1])
				snake.pop(0)


		if direction_change == True:
			direction_change = False


	pygame.display.flip()

pygame.quit()