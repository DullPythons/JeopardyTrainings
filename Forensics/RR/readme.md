# RR

One of my drives failed and need help recovering all my files. As far as I know the persons who have set up my PC used something like Reusing All of Internal Disks https://drive.google.com/file/d/1b6FfX2fBDALtOMF4-R-PwLCB27jC1vEo/view?usp=sharing

Flag format: HackTM{}

# Решение

В этом задании нам дали архив с тремя изображениями.

Смотрим их свойства и замечаем, что два из них весят по 512 мбайт, а третий не имеет данных вовсе. Приходим к выводу, что задача связана с RAID recovery. <br/>
Самый простой вариант это XORить два файла между собой, для этого используем утилиту XorFiles (https://www.nirsoft.net/utils/xorfiles.html) <br/>
Получили утерянный диск, дальше можно смонтировать его и искать флаг там, но если посмотреть на hex этого файла, то можно увидеть заголовок jpeg.<br/>
Копируем нужные байты, загоняем их в HexEditor и сохраняем файл с расширением .jpeg<br/>
Открываем полученное изображение и видим флаг.

## вариант от @Neprincessa

Так же в качестве утилит для ксора файлов можно использовать https://github.com/scangeo/xor-files
`./xor-files -r ~/Downloads/Images/res.img ~/Downloads/Images/1.img ~/Downloads/Images/3.img`<br/>
Получили образ, как говорилось выше, заметили, что там картинка, можно вытащить с помощью: `dd if=~/Downloads/Images/res.img of=~/Downloads/Images/extr_1.jpeg bs=1 skip=69476352 count=90000`<br/>
Там флаг: HackTM{1bf965b6e23e5d2cb4bdfa67b6d8b0940b5a23e98b8593bb96a4261fb8a1f66a}
