import pygame, main

pygame.init()
WIDTH, HEIGHT = 900, 600
WHITE = (255, 255, 255)
GREY = (125, 125, 125)
BLACK = (0, 0, 0)
FPS = 60
MY_FONT = pygame.font.SysFont('sans', 18)
MY_FONT_2 = pygame.font.SysFont('sans', 13)
color_for_button = GREY
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('dieu phoi FIFO!')
active = False
active_2 = False
active_3 = False

temp = 1

NUM_OF_PROCESS = ''
TIME_RL = ''
TIME_CPU = ''
text_1 = MY_FONT.render("number of process: ", 1, BLACK)
text_10 = MY_FONT.render("enter timeRL: ", 1, BLACK)
text_12 = MY_FONT.render("enter timeCPU: ", 1, BLACK)
text_13 = MY_FONT.render(f"enter information for process {temp}:", 1, BLACK)
input_rect = pygame.Rect(7 + text_1.get_width() + 135, 80, 37, 25)
input_rect_2 = pygame.Rect(3 + text_10.get_width(), 195, 73, 35)
input_rect_3 = pygame.Rect(3 + text_12.get_width(), 255, 60, 35)
input_rect_for_mouse = pygame.Rect(270, 192, 100, 100)

process_list = []
time_loop = 0


def logic_handle():
    global NUM_OF_PROCESS, TIME_RL, TIME_CPU, time_loop, temp, text_13, process_list

    if NUM_OF_PROCESS != '':
        for i in range(int(NUM_OF_PROCESS)):
            if not process_list:
                TIME_RL = '0'

            process_name = f'P{i + 1}'

            if TIME_RL != '' and TIME_CPU != '' and time_loop < int(NUM_OF_PROCESS):
                if main.check_time(process_list, int(TIME_RL)):
                    TIME_RL = ''
                    error_warn_1 = MY_FONT.render("trung thoi gian vao ready list", 1, BLACK)
                    WIN.blit(error_warn_1, (text_10.get_width() + 5 + 50, 203))

                else:
                    process_obj = main.Process(process_name, int(TIME_RL), int(TIME_CPU))
                    process_list.append(process_obj)
                    TIME_RL = ''
                    TIME_CPU = ''
                    time_loop += 1
                    if temp != int(NUM_OF_PROCESS):
                        temp += 1

    process_list.sort(key=lambda p: p.rl_time)


def draw_window(input_rectangle, ip_rect2, ip_rect3, rect_mouse):
    global text_13
    WIN.fill((255, 153, 102))
    text_13 = MY_FONT.render(f"enter information for process {temp}:", 1, BLACK)
    pygame.draw.rect(WIN, (255, 92, 51), (175, 0, 100, 50))  # input
    pygame.draw.rect(WIN, (255, 92, 51), (625, 0, 100, 50))  # output
    # pygame.draw.rect(WIN, GREY, (475, 450, 400, 100))  # thoi gian cho trung binh
    pygame.draw.rect(WIN, GREY, (475, 500, 400, 75))
    pygame.draw.rect(WIN, color_for_button, rect_mouse)  # nut bam
    text_button = MY_FONT.render("RESET", 1, BLACK)
    WIN.blit(text_button, (320 - text_button.get_width() / 2, 242 - text_button.get_height() / 2))
    pygame.draw.rect(WIN, GREY, (450, 0, 3, HEIGHT))  # vach ke doc
    pygame.draw.rect(WIN, GREY, (135, 70, 180, 45), 2)  # so luong tien trinh
    pygame.draw.rect(WIN, GREY, (0, 130, 230, 45), 2)  # 3 o moi
    pygame.draw.rect(WIN, GREY, (0, 190, 180, 45), 2)
    pygame.draw.rect(WIN, GREY, (0, 250, 180, 45), 2)
    pygame.draw.rect(WIN, GREY, (25, 120 + 200, 70, 25), 2)  # O1
    pygame.draw.rect(WIN, GREY, (175, 120 + 200, 70, 25), 2)
    pygame.draw.rect(WIN, GREY, (325, 120 + 200, 70, 25), 2)
    pygame.draw.rect(WIN, GREY, (465, 120, 50, 25), 2)  # X1
    pygame.draw.rect(WIN, GREY, (540, 120, 50, 25), 2)
    pygame.draw.rect(WIN, GREY, (615, 120, 50, 25), 2)
    pygame.draw.rect(WIN, GREY, (690, 120, 50, 25), 2)
    pygame.draw.rect(WIN, GREY, (765, 120, 50, 25), 2)
    pygame.draw.rect(WIN, GREY, (840, 120, 50, 25), 2)

    text_2 = MY_FONT.render("INPUT", 1, BLACK)
    text_3 = MY_FONT.render("OUTPUT", 1, BLACK)
    text_4 = MY_FONT_2.render("name", 1, BLACK)
    text_5 = MY_FONT_2.render("timeRL", 1, BLACK)
    text_6 = MY_FONT_2.render("timeCPU", 1, BLACK)
    text_7 = MY_FONT_2.render("timeIn", 1, BLACK)
    text_8 = MY_FONT_2.render("timeOut", 1, BLACK)
    text_9 = MY_FONT_2.render("timeWait", 1, BLACK)

    if active:
        color1 = BLACK
    else:
        color1 = GREY
    pygame.draw.rect(WIN, color1, input_rect, 2)
    render_num = MY_FONT.render(NUM_OF_PROCESS, 1, BLACK)
    WIN.blit(render_num, (10 + text_1.get_width() + 135, 82))

    if active_2:
        color2 = BLACK
    else:
        color2 = GREY
    pygame.draw.rect(WIN, color2, ip_rect2, 2)
    render_t1 = MY_FONT.render(TIME_RL, 1, BLACK)
    WIN.blit(render_t1, (5 + text_10.get_width(), 203))

    if active_3:
        color3 = BLACK
    else:
        color3 = GREY
    pygame.draw.rect(WIN, color3, ip_rect3, 2)
    render_t2 = MY_FONT.render(TIME_CPU, 1, BLACK)
    WIN.blit(render_t2, (5 + text_12.get_width(), 263))

    WIN.blit(text_1, (10 + 135, 80))
    WIN.blit(text_2, (225 - text_2.get_width() / 2, 25 - text_2.get_height() / 2))
    WIN.blit(text_3, (675 - text_3.get_width() / 2, 25 - text_3.get_height() / 2))
    WIN.blit(text_4, (60 - text_4.get_width() / 2, 132.5 - text_4.get_height() / 2 + 200))
    WIN.blit(text_4, (490 - text_4.get_width() / 2, 132.5 - text_4.get_height() / 2))
    WIN.blit(text_5, (210 - text_5.get_width() / 2, 132.5 - text_5.get_height() / 2 + 200))
    WIN.blit(text_5, (565 - text_5.get_width() / 2, 132.5 - text_5.get_height() / 2))
    WIN.blit(text_6, (360 - text_6.get_width() / 2, 132.5 - text_6.get_height() / 2 + 200))
    WIN.blit(text_6, (640 - text_6.get_width() / 2, 132.5 - text_6.get_height() / 2))
    WIN.blit(text_7, (715 - text_7.get_width() / 2, 132.5 - text_7.get_height() / 2))
    WIN.blit(text_8, (790 - text_8.get_width() / 2, 132.5 - text_8.get_height() / 2))
    WIN.blit(text_9, (865 - text_9.get_width() / 2, 132.5 - text_9.get_height() / 2))
    WIN.blit(text_13, (3, 152.5 - text_13.get_height() / 2))
    WIN.blit(text_10, (3, 212.5 - text_10.get_height() / 2))
    WIN.blit(text_12, (3, 272.5 - text_12.get_height() / 2))

    line_spacing = 30
    first_line = 120
    for process in process_list:
        pygame.draw.rect(WIN, GREY, (25, first_line + line_spacing + 200, 70, 25), 2)  # O2
        pygame.draw.rect(WIN, GREY, (175, first_line + line_spacing + 200, 70, 25), 2)
        pygame.draw.rect(WIN, GREY, (325, first_line + line_spacing + 200, 70, 25), 2)
        first_line = first_line + line_spacing

    line_spacing_2 = 30
    first_line_2 = 120
    for process in process_list:
        pygame.draw.rect(WIN, GREY, (465, first_line_2 + line_spacing_2, 50, 25), 2)  # X2
        pygame.draw.rect(WIN, GREY, (540, first_line_2 + line_spacing_2, 50, 25), 2)
        pygame.draw.rect(WIN, GREY, (615, first_line_2 + line_spacing_2, 50, 25), 2)
        pygame.draw.rect(WIN, GREY, (690, first_line_2 + line_spacing_2, 50, 25), 2)
        pygame.draw.rect(WIN, GREY, (765, first_line_2 + line_spacing_2, 50, 25), 2)
        pygame.draw.rect(WIN, GREY, (840, first_line_2 + line_spacing_2, 50, 25), 2)
        first_line_2 += line_spacing_2

        i = 1
        first_line_3 = 132.5
        line_spacing_3 = 30
    for process in process_list:
        process_name = MY_FONT_2.render(f"P{i}", 1, BLACK)
        i += 1
        WIN.blit(process_name, (
            60 - process_name.get_width() / 2, first_line_3 + line_spacing_3 - process_name.get_height() / 2 + 200))
        first_line_3 += line_spacing

        j = 1
        first_line_4 = 132.5
        line_spacing_4 = 30
    for process in process_list:
        process_name = MY_FONT_2.render(f"P{j}", 1, BLACK)
        j += 1
        WIN.blit(process_name,
                 (490 - process_name.get_width() / 2, first_line_4 + line_spacing_4 - process_name.get_height() / 2))
        first_line_4 += line_spacing_4

    sum_of_wait_time = 0
    state = 0
    line_spacing_5 = 30
    first_line_5 = 362.5 - 30
    line_spacing_6 = 30
    first_line_6 = 362.5 - 30
    first_line_7 = 132.5
    line_spacing_7 = 30
    for process in process_list:
        sum_of_wait_time = sum_of_wait_time + max(main.wait_time(process, state), 0)
        wait_time = max(main.wait_time(process, state), 0)
        state = max(state, process.rl_time) + process.p_time
        temp_out = MY_FONT_2.render(str(state), 1, BLACK)

        temp_wait = MY_FONT_2.render(str(wait_time), 1, BLACK)

        # xuat ra man hinh
        temp_rl = MY_FONT_2.render(str(process.rl_time), 1, BLACK)
        temp_cpu = MY_FONT_2.render(str(process.p_time), 1, BLACK)
        WIN.blit(temp_rl, (210 - temp_rl.get_width() / 2, first_line_5 - temp_rl.get_height() / 2 + line_spacing_5))
        WIN.blit(temp_rl, (565 - temp_rl.get_width() / 2, first_line_7 - temp_rl.get_height() / 2 + line_spacing_7))
        WIN.blit(temp_cpu, (640 - temp_cpu.get_width() / 2, first_line_7 - temp_cpu.get_height() / 2 + line_spacing_7))
        WIN.blit(temp_out, (790 - temp_out.get_width() / 2, first_line_7 - temp_out.get_height() / 2 + line_spacing_7))
        WIN.blit(temp_wait,
                 (865 - temp_wait.get_width() / 2, first_line_7 - temp_wait.get_height() / 2 + line_spacing_7))
        first_line_7 += line_spacing_7
        first_line_5 += line_spacing_5

        WIN.blit(temp_cpu, (360 - temp_cpu.get_width() / 2, first_line_6 - temp_cpu.get_height() / 2 + line_spacing_6))

        first_line_6 += line_spacing_6

    if len(process_list):
        average_time = round(sum_of_wait_time / len(process_list), 2)
        average_render = MY_FONT.render("AVERAGE WAIT TIME: " + str(average_time) + " ms", 1, BLACK)
        WIN.blit(average_render, (675 - average_render.get_width() / 2, 387.5 - average_render.get_height() / 2 + 150))
        if TIME_RL != '':
            if main.check_time(process_list, int(TIME_RL)):
                error_warn_1 = MY_FONT.render("coincident", 1, BLACK)
                error_warn_2 = MY_FONT.render("time in RL", 1, BLACK)
                error_warn_3 = MY_FONT.render("pls re-enter", 1, BLACK)
                WIN.blit(error_warn_1, (text_10.get_width() + 95, 180))
                WIN.blit(error_warn_2, (text_10.get_width() + 95, 180 + error_warn_1.get_height()))
                WIN.blit(error_warn_3,
                         (text_10.get_width() + 95, 180 + error_warn_1.get_height() + error_warn_2.get_height()))
            else:
                error_warn_1 = MY_FONT.render("", 1, BLACK)

    time_in = 0
    first_line_8 = 132.5
    control = 0
    for process in process_list:
        time_in = max(time_in, process.rl_time)
        temp_in_render = MY_FONT_2.render(str(time_in), 1, BLACK)
        WIN.blit(temp_in_render,
                 (715 - temp_in_render.get_width() / 2, first_line_8 - temp_in_render.get_height() / 2 + line_spacing_7))
        first_line_8 += line_spacing_7
        control += 1
        time_in += process.p_time
        if control >= len(process_list):
            break
    pygame.display.update()


def ui():
    global active, active_2, active_3, process_list, time_loop, color_for_button, temp

    global NUM_OF_PROCESS, TIME_RL, TIME_CPU
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect_2.collidepoint(event.pos):
                    active_2 = True
                else:
                    active_2 = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect_for_mouse.collidepoint(event.pos):
                    color_for_button = (153, 102, 51)
                    process_list = []
                    NUM_OF_PROCESS = ''
                    TIME_RL = ''
                    TIME_CPU = ''
                    time_loop = 0
                    temp = 1
                elif input_rect_3.collidepoint(event.pos):
                    active_3 = True
                else:
                    color_for_button = GREY
                    active_3 = False

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        NUM_OF_PROCESS = NUM_OF_PROCESS[0:-1]
                    else:
                        if event.unicode.isdigit():
                            NUM_OF_PROCESS += event.unicode
                        if event.key == pygame.K_RETURN:
                            # NUM_OF_PROCESS = NUM_OF_PROCESS[0:-1]
                            active = False
                            logic_handle()
                if active_2:
                    if event.key == pygame.K_BACKSPACE:
                        TIME_RL = TIME_RL[0:-1]
                    else:
                        if event.unicode.isdigit():
                            TIME_RL += event.unicode
                        if event.key == pygame.K_RETURN:
                            # TIME_RL = TIME_RL[0:-1]
                            active_2 = False
                            logic_handle()
                if active_3:
                    if event.key == pygame.K_BACKSPACE:
                        TIME_CPU = TIME_CPU[0:-1]
                    else:
                        if event.unicode.isdigit():
                            TIME_CPU += event.unicode
                        if event.key == pygame.K_RETURN:
                            # TIME_CPU = TIME_CPU[0:-1]
                            active_3 = False
                            logic_handle()

        draw_window(input_rect, input_rect_2, input_rect_3, input_rect_for_mouse)

    pygame.quit()


ui()
