### 1. pygame 선언

import pygame
pygame.init()       # pygame initializing

### 2. pygame에 사용되는 전역변수 선언
Color = (255, 255, 255) # white color
size = [400, 300]
screen = pygame.display.set_mode(size)
done = False
clock = pygame.time.Clock()

### 추가 코드
# pygame에 사용할 수 있도록 블리츠크랭크 이미지를 호출
blitz = pygame.image.load('blitzcrank.png')
blitz = pygame.transform.scale(blitz, (200, 200))     # 이미지 스케일링

### 3. pygame 무한 루프 : 게임 본체
def runGame():
    global done, blitz
    blitz_x = 0
    blitz_y = 0

    while not done:
        clock.tick(10)
        screen.fill(Color)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:       # 게임 화면 종료
                done = True
            if event.type == pygame.KEYDOWN:        # 현재는 화면 밖으로 나가는 현상 발생
                if event.key == pygame.K_UP:
                    blitz_y -= 10
                elif event.key == pygame.K_DOWN:
                    blitz_y += 10
                elif event.key == pygame.K_LEFT:
                    blitz_x -= 10
                elif event.key == pygame.K_RIGHT:
                    blitz_x += 10

        screen.blit(blitz, (blitz_x, blitz_y))
        pygame.display.update()     # 게임 화면 업데이트

### 4. pygame 게임 종료
runGame()
pygame.quit()