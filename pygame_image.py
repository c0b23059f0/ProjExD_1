import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img_r = pg.transform.flip(bg_img, True, False)
    kt_img = pg.image.load("fig/3.png")
    kt_img = pg.transform.flip(kt_img, True, False)
    tmr = 0
    bg_x = 0
    kt_rec = kt_img.get_rect()
    kt_rec.center = 300, 200
    screen.blit(kt_img, kt_rec)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        keys = pg.key.get_pressed()
        
        move_x, move_y = 0, 0
        if keys[pg.K_UP]:
            move_y -= 1
        if keys[pg.K_DOWN]:
            move_y += 1
        if keys[pg.K_RIGHT]:
            move_x += 2
        if keys[pg.K_LEFT]: 
            move_x -= 2
        else:
            move_x -= 1  
        kt_rec.move_ip(move_x, move_y)

        bg_x = -(tmr%3200)
        screen.blit(bg_img_r, [bg_x+1600, 0])
        screen.blit(bg_img, [bg_x, 0])
        screen.blit(bg_img_r, [(bg_x+4800), 0])
        screen.blit(bg_img, [(bg_x+3200), 0])
        #screen.blit(bg_img, [0, 0])
        screen.blit(kt_img, kt_rec)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()