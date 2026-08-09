from cr3bp_code_final import simulation
from Lagrange_point_final import main
import pygame

mu = 0.0121545352
main()   
print("--"*26)

pygame.init()
width, height = 1000, 700
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("CR3BP")
clock = pygame.time.Clock()

X, Y = -1.5, 1.5
def math_screen(x,y):
    x_normal = (x - X)/(Y - X)
    y_normal = (y - X)/(Y - X)
    x_pixel = int(x_normal * width)
    y_pixel = int((1 - y_normal) * height)
    return x_pixel, y_pixel

def screen_math(x_pixel, y_pixel):
    x_normal = x_pixel / width
    y_normal = 1 - (y_pixel / height)
    x = X + x_normal * (Y - X)
    y = X + y_normal * (Y - X)
    return x, y

t, math = simulation(0.8368956930433207 ,0.0) # <--- Here change the initial coordinate !
                                                  # You can take from console output ;)
current_frame = 0
run = True
while run:
    window.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_po, y_po = pygame.mouse.get_pos()
            x_data, y_data = screen_math(x_po, y_po)
            t, math = simulation(x_data, y_data)
            print("Calculating new Initial coordinate:")
            print(f"X = {x_data:.16f} , Y = {y_data:.16f}")
            print("--"*26)
            current_frame = 0
        
    earth_x, earth_y = math_screen(mu, 0)
    moon_x, moon_y = math_screen((1 - mu), 0)
    pygame.draw.circle(window, (0,128,255), (earth_x, earth_y), 15)
    pygame.draw.circle(window, (192,192,192), (moon_x,moon_y), 5)
    
    if current_frame < len(math[0]) - 1:
        current_frame += 10
    if current_frame > 1:
        point = []
        for i in range(current_frame):
            x = math[0][i]
            y = math[1][i]
            px, py = math_screen(x, y)
            point.append((px,py))
        pygame.draw.lines(window,(255,255,153), False, point,2)
        pygame.draw.circle(window, (153, 255, 255), point[-1], 3)
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

if __name__== "__main__":
    pass

