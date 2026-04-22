import psutil
from datetime import datetime
from time import sleep

log_file = open('system_log.txt', 'w')

try:
    while True:
        cpu_list = psutil.cpu_percent(interval=1, percpu=True)
        cpu_avg = sum(cpu_list) / len(cpu_list)

        # --- BƯỚC 7: Logic phân loại 3 mức cảnh báo ---
        if cpu_avg >= 70:
            status = 'CRITICAL'
        elif cpu_avg >= 30:
            status = 'WARNING'
        else:
            status = 'NORMAL'

        ram = psutil.virtual_memory()
        ram_used_mb = ram.used // (1024 ** 2)
        ram_total_mb = ram.total // (1024 ** 2)
        ram_pct = ram.percent

        disk = psutil.disk_usage('/')
        disk_pct = disk.percent

        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # --- BƯỚC 7: Cập nhật biến line, nhét thêm {status} vào cuối ---
        line = (f'[{now}] CPU: {cpu_avg:.1f}% | '
                f'RAM: {ram_used_mb}/{ram_total_mb} MB ({ram_pct}%) | Disk: {disk_pct}% | {status}')
        print(line)
        # --- BƯỚC 7: In dòng riêng nếu có biến (cảnh báo) ---
        if status != 'NORMAL':
            print(f' ⚠ {status}: CPU đang ở {cpu_avg:.1f}%')

        log_file.write(line + '\n')
        log_file.flush()
        sleep(2)

except KeyboardInterrupt:
    print('\nDừng giám sát.')
finally:
    log_file.close()
    print('Log saved to system_log.txt')
