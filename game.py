import pygame, vector, matrix, math, shape, random

def renderShape(surface, shape, middle, color=0xFFFFFF):
    pygame.draw.polygon(surface, color, shape.getPointPairs(middle))
    #pygame.draw.circle(surface, 0xFF00FF, shape.mp_pair(middle), 5)

def main(width, height):
    squares = []
    colors = []

    number = 10
    for y in range(-1, number + 1):
        for x in range(-1, number + 1):
            squares.append(shape.Shape.rectangle(x * width  /number - width / 2, y * height / number - height / 2, width / number + 1, height / number + 1))
            colors.append(random.randint(0, 0xFFFFFF))


    middle = vector.Vector(width / 2, height / 2)

    pygame.init()

    screen = pygame.display.set_mode((width, height))



    running = True
    fps = 0
    last = pygame.time.get_ticks()
    while running:
        screen.fill(0)






        for index,square in enumerate(squares):
            square.rotate(pow(-1, index) *math.pi / 100)
            renderShape(screen, square, middle, colors[index])
            square.translate(vector.Vector(-5, 1))
            if square.mp.y > height / 2 + height / number:
                square.translate(vector.Vector(0, -height - 2 * height / number))
            if square.mp.x < -width / 2 - width / number:
                square.translate(vector.Vector(width + 2 * width / number, 0))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False

        fps = fps + 1
        pygame.time.delay(8)
        now = pygame.time.get_ticks()
        if now - last > 1000:
            last = now
            print(fps)
            fps = 0

if __name__ == '__main__':
    main(600, 600)
