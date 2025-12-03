'An analogue of Steam'

# You are writing an installer program for a computer game. While the installer downloads the update, it is necessary for the user to display the number of percentages downloaded so that he understands whether he will have time to brew tea before the process is completed. Each game update requires a different number of megabytes, while different players have different Internet connection speeds.

# What needs to be done

# Write a program that accepts the input of the update file size in megabytes and the Internet connection speed in megabytes per second. For each second, the program must calculate and display the percentage of downloaded volume until the download is completed. At the end, the program should show how many seconds it took to download the update. Provide input control.


'Аналог Steam'

# Вы пишете программу-инсталлятор для компьютерной игры. Пока инсталлятор скачивает обновление, для пользователя необходимо отображать количество скачанных процентов, чтобы он понимал, успеет ли заварить чай, прежде чем завершится процесс. Каждое обновление игры требует разного количества мегабайтов, при этом у разных игроков разная скорость интернет-соединения.

# Что нужно сделать

# Напишите программу, принимающую на вход размер файла обновления в мегабайтах и скорость интернет-соединения в мегабайтах в секунду. Для каждой секунды программа должна рассчитывать и выводить на экран процент скачанного объёма до тех пор, пока скачивание не завершится. В конце программа должна показать, сколько секунд заняло скачивание обновления. Обеспечьте контроль ввода.

# ---------------------------------------------------------------------

download_size = int(input("Введите размер обновления в мегабайтах: "))
download_speed = int(input("Введите скорость скачивания мб/сек: "))
percent = download_size / 100
download_counter = 0
percent_counter = 0

if download_size < 0 or download_speed < 0:
        print("Размер обновления и скорость соединения не могут быть меньше нуля.")
        exit()

for second in range(1, download_size // download_speed + 2):
    if (download_size - download_counter) < download_speed:
        download_counter = download_size
        percent_counter = 100
        print("Прошло", second, "сек.Скачано", download_counter, "из", download_size, "-", percent_counter, "%")
    else:
        download_counter += download_speed
        percent_counter = download_counter / percent
        print("Прошло", second, "сек.Скачано", download_counter, "из", download_size, "-", int(round(percent_counter)), "%")