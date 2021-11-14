# logic first then the UI
def wait_time(current_process, state):
    return state - current_process.rl_time


def check_time(processes, time_entered):
    for process in processes:
        if time_entered == process.rl_time:
            return True
    return False


class Process:
    def __init__(self, p_name, rl_time, p_time):
        self.p_name = p_name
        self.rl_time = rl_time
        self.p_time = p_time


def main():
    process_list = []
    num_of_process = int(input('nhap so luong tien trinh:'))
    for i in range(num_of_process):
        process_name = str(input('nhap process name: '))
        if not process_list:
            time_enter_rl = 0
            print(f'tien trinh dau tien thoi gian vao ready list la {time_enter_rl}')
        else:
            time_enter_rl = int(input('nhap thoi gian vao ready list: '))
            while check_time(process_list, time_enter_rl):
                print('error: trung thoi gian vao ready list!! \n')
                print(f'thoi gian vao ready list cua cac tien trinh da nhap la: \n')
                for process in process_list:
                    print('process name     Time RL')
                    print(f'     {process.p_name}              {process.rl_time}')
                time_enter_rl = int(input('nhap lai thoi gian vao ready list: '))
        process_time = int(input('nhap thoi gian xu ly: '))
        process_obj = Process(process_name, time_enter_rl, process_time)
        process_list.append(process_obj)

    sum_of_wait_time = 0
    state = 0


    process_list.sort(key=lambda p: p.rl_time)
    for process in process_list:
        sum_of_wait_time = sum_of_wait_time + wait_time(process, state)
        state = state + process.p_time
        print(f'state la: {state} xong tien trinh {process.p_name}')

    average_wait_time = sum_of_wait_time / len(process_list)
    print(f'thoi gian cho trung binh la: {round(average_wait_time, 2)}')


if __name__ == "__main__":
    main()
