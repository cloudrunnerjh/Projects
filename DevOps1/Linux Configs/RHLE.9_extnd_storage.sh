
#After increasing the VM's hard disk size from Edit Settings, pesent this change to the internal Guest OS by following the below steps.
#To extend the logical volume:
#Caution: VMware recommends to take a complete backup of the virtual machine prior to making these changes.
#Power off the virtual machine.
#Edit the virtual machine settings and extend the virtual disk size. For more information, see Increasing the size of a virtual disk .
#Power on the virtual machine.
#Identify the device name, which is by default /dev/sda, and confirm the new size by running the command:
fdisk -l
#Create a new primary partition:
#Run the command:
fdisk /dev/sda
# (depending the results of the step 4)
# Press p to print the partition table to identify the number of partitions. By default, there are 2: sda1 and sda2.
#Press n to create a new primary partition.
#Press p for primary.
#Press 3 for the partition number, depending on the output of the partition table print.
#Press Enter two times.
#Press t to change the system's partition ID.
#Press 3 to select the newly creation partition.
#Type 8e to change the Hex Code of the partition for Linux LVM.
#Press w to write the changes to the partition table.
#Restart the virtual machine.
#Run this command to verify that the changes were saved to the partition table and that the new partition has an 8e type:
fdisk -l
#Run this command to convert the new partition to a physical volume:
#Note: The number for the sda can change depending on system setup. Use the sda number that was created in step 5.
pvcreate /dev/sda3
#Run this command to extend the physical volume:
#Note: To determine which volume group to extend, use the command vgdisplay
#Note: Additionally, for the remainder of the commands, VolGroup00 will be unique to each Guest and should be adjusted to reflect the affected specific VM.
vgextend VolGroup00 /dev/sda3
#Run this command to verify how many physical extents are available to the Volume Group:
vgdisplay VolGroup00 | grep "Free"
#Run the following command to extend the Logical Volume:
#Note: To determine which logical volume to extend, use the command lvdisplay.
lvextend -L+#G /dev/VolGroup00/LogVol00
Where # is the number of Free space in GB available as per the previous command. Use the full number output from Step 10 including any decimals.
#Run the following command to expand the ext3 filesystem online, inside of the Logical Volume:
#Note:
#Use resize2fs instead of ext2online for non-Red Hat virtual machines.
#Use xfs_growfs for Red Hat, CentOS 7 and other VM Guest OS types that use the XFS file system.
ext2online /dev/VolGroup00/LogVol00
#Run the following command to verify that the / filesystem has the new space available:
df -h /
#Note: Defer to Red Hat or Cent OS for maximum size for logical volumes based on OS versions.
