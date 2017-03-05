import pygame, vector, matrix, math, shape

def renderShape(surface, shape, middle, color=0xFFFFFF):
    pygame.draw.polygon(surface, color, shape.getPointPairs(middle))

def main():
    triangle = shape.Shape([vector.Vector(-100, -100), vector.Vector(100, -100), vector.Vector(0, 50)])
    #square.translate(vector.Vector(0, 10))

    width = 600
    height = 500

    middle = vector.Vector(width / 2, height / 2)

    pygame.init()

    screen = pygame.display.set_mode((width, height))



    running = True
    fps = 0
    last = pygame.time.get_ticks()
    while running:
        screen.fill(0)

        renderShape(screen, triangle, middle)

        pygame.display.flip()


        triangle.rotate(math.pi/1000)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False

        fps = fps + 1
        #pygame.time.delay(16)
        now = pygame.time.get_ticks()
        if now - last > 1000:
            last = now
            print(fps)
            fps = 0

if __name__ == '__main__':
    main()
