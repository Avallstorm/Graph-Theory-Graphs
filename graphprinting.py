from pygame.locals import *
import pygame.draw
import math, sys
import re

#===============================================================================
#Data

#Data for a full graph
if "S" in sys.argv:
	VERTICIES = int(sys.argv[1])
	EDGES = []
	for i in range(VERTICIES):
		for j in range(i,VERTICIES):
			EDGES += [(i,j)]

#Data for a cycle
if "C" in sys.argv:
	VERTICIES = int(sys.argv[1])
	EDGES = []
	for i in range(VERTICIES):
		EDGES += [(i,(i+1)%VERTICIES)]

#Data for a maximal matching
if "matching" in sys.argv:
	VERTICIES = int(sys.argv[1])
	EDGES = []
	for i in range(int(VERTICIES/2)):
		EDGES += [(i*2,(i*2)+1)]

#Data for maximal triangles
if "triangles" in sys.argv:
	VERTICIES = int(sys.argv[1])
	EDGES = []
	for i in range(int(VERTICIES/3)):
		EDGES += [(i*3,(i*3)+1)]
		EDGES += [(i*3,(i*3)+2)]
		EDGES += [((i*3)+1,(i*3)+2)]

#Data for free edges
if "free" in sys.argv:
	VERTICIES = int(sys.argv[1])
	EDGES = []
	#user input loop
	while(1):
		userin = input("Please entre edge of the form (x,y): ")
		if "exit" in userin or "stop" in userin:
			break
		elif "help" in userin:
			print("help,exit,display")
		elif "show" in userin or "display" in userin:
			print(EDGES)
		elif "," in userin and "(" in userin and ")" in userin:
			edgeval = list(map(int,re.findall('\d+', userin)))
			if len(edgeval) == 2:
				EDGES += [(edgeval[0],edgeval[1])]
		else:
			print("Not a command or misformed edge")

#===============================================================================
#Constants 

TESTING = False

DISTANCE = 300

ANGEL = math.pi*2/VERTICIES

#===============================================================================

def main():
	vertlist = []
	#Set position for the vertices
	for i in range(VERTICIES):
		vertlist += [(400 + int(math.sin(ANGEL*i)*DISTANCE)\
			,int(400 + math.cos(ANGEL*i)*DISTANCE))]

	#Setup for pygame
	pygame.init()
	screen = pygame.display.set_mode((800,800))
	myfont = pygame.font.SysFont("monospace", 17)

	while(1):

		#Pygame event loop
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		#Screen filling
		screen.fill((255,255,255))

		#Drawing edges on the screen
		for edge in EDGES:
			x,y = vertlist[edge[0]],vertlist[edge[1]]
			pygame.draw.line(screen, (0,0,0), x, y, 5)

		#Drawing vertices on screen
		for i in range(len(vertlist)):
			vert = vertlist[i]
			label = myfont.render("{0}".format(i), 1, (255,255,255))
			pygame.draw.circle(screen,(0,0,0),vert,15)
			screen.blit(label,(vert[0] - 5, vert[1] - 8))

		#Saving the screen as a picture and ending the program
		if not TESTING:
			pygame.image.save(screen,"Graph.PNG")
			break
		pygame.display.flip()

if __name__ == '__main__':
	main()
