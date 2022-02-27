# READ ME FOR RASPBERRY PICO

#SELF-NOTES
-------------------
Mount Pico
-------------------
1. Hold down the BOOTSEL button and connect the Raspberry Pi Pico to your PC via micro USB cable. Once Pico is connected release the BOOTSEL button. This button puts Raspberry Pi Pico into USB mass storage device mode.

2. Find the USB mass storage device called RPI-RP2:
sudo blkid -o list | grep RPI-RP2

#An example of output:
#/dev/sdb1  vfat    RPI-RP2  (not mounted)  0034-04C4

3. Create a new directory: (If mount doesn't exist)
sudo mkdir /mnt/pico

4. Mount device to /mnt/pico directory:
sudo mount /dev/sdb1 /mnt/pico

5. Check files in /mnt/pico:
ls /mnt/pico

#If you can see the following files then the USB mass storage device has been mounted correctly: 
#INDEX.HTM  INFO_UF2.TXT

-------------------
COPY FILE AND SYNC PICO
-------------------
1. Copy program into storage device:
sudo cp myapp.uf2 /mnt/pico

2. Flush memory buffer to the storage device:
sudo sync

#Raspberry Pi Pico will disconnect as a USB mass storage device and runs the code.

#Note: if you want to upload new code to the Raspberry Pi Pico, disconnect it from power and hold down the BOOTSEL button when connecting Pico to power.
