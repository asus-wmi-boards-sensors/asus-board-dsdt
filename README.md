# asus-board-dsdt

Collection of DSDT files required for support of https://bugzilla.kernel.org/show_bug.cgi?id=204807

All files are provided by motherboard users or downloaded and extracted from support section of ASUS website.

Support sites:
* [ASUS UEFI](https://www.asus.com/motherboards-components/motherboards/all-series/)
* [ASUS ACPI DUMPS](https://github.com/linuxhw/ACPI/tree/master/Desktop/ASUSTek%20Computer)
* [ASUS DMI DUMPS](https://github.com/linuxhw/DMI/tree/master/Desktop/ASUSTek%20Computer)
* [Gigabyte UEFI](https://www.gigabyte.com/Motherboard/All-Series)
* [NCT* sensors](https://www.nuvoton.com/)

# Docs

How it works for:
* [ASUS](https://bugzilla.kernel.org/show_bug.cgi?id=204807#c37)
* [Gigabyte](https://github.com/t-8ch/linux-gigabyte-wmi-driver)
* [it87](https://github.com/frankcrawford/it87)
* [ACPI Specification](https://uefi.org/specifications)
* [HWMON repository](https://git.kernel.org/pub/scm/linux/kernel/git/groeck/linux-staging.git/log/?h=hwmon-next)
* [NetBSD](https://github.com/NetBSD/src/tree/trunk/sys/dev/isa/wbsio.c)
* [NetBSD nct6799D](https://github.com/NetBSD/src/commit/8320b6cc18fa066411b30896566869b05eb29ed7)

Datasheets for sensors are placed to [docs directory](docs).

* [Used Super I/O Chips](docs/linuxhw_DMI.csv)
* [NCT6776F/D](https://media.digikey.com/pdf/Data%20Sheets/Nuvoton%20PDFs/NCT6776F,D.pdf)
* [NCT6796D](https://www.nuvoton.com/export/resource-files/NCT6796D_Datasheet_V0_6.pdf)
* search more in google: `site:www.nuvoton.com nct6 pdf`

# Supported boards

| made by  | board name                       | superio    | asus_wmi_sensors (io mutex)   | gigabyte-wmi | nct6775 (io mutex)            | asus_ec_sensors (ec mutex)    |
| ---------| -------------------------------- | ---------- | ----------------------------- | ------------ | ----------------------------- | ----------------------------- |
| ASUS     | 970 PRO GAMING/AURA              |            | N                             | N            | N                             | N                             |
| ASUS     | A68HM-K                          |            | N                             | N            | N                             | N                             |
| ASUS     | A68HM-PLUS                       |            | N                             | N            | N                             | N                             |
| ASUS     | A88X-GAMER                       |            | N                             | N            | N                             | N                             |
| ASUS     | B150 PRO GAMING                  | NCT6793D   | N                             | N            | P (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | B150 PRO GAMING D3               | NCT6793D   | N                             | N            | P (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | B150 PRO GAMING/AURA             |            | N                             | N            | N                             | N                             |
| ASUS     | B150I PRO GAMING/AURA            | NCT5539D   | N                             | N            | P (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | B150I PRO GAMING/WIFI/AURA       | NCT5539D   | N                             | N            | P (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | B150M PRO GAMING                 | NCT6793D   | N                             | N            | P (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| GIGABYTE | B450M DS3H-CF                    |            | N                             | L            | N                             | N                             |
| GIGABYTE | B450M S2H V2                     |            | N                             | L            | N                             | N                             |
| GIGABYTE | B550 AORUS ELITE                 |            | N                             | L            | N                             | N                             |
| GIGABYTE | B550 AORUS ELITE AX V2           |            | N                             | L            | N                             | N                             |
| GIGABYTE | B550 AORUS ELITE V2              |            | N                             | L            | N                             | N                             |
| GIGABYTE | B550 GAMING X V2                 |            | N                             | L            | N                             | N                             |
| GIGABYTE | B550I AORUS PRO AX               |            | N                             | L            | N                             | N                             |
| GIGABYTE | B550M AORUS PRO-P                |            | N                             | L            | N                             | N                             |
| GIGABYTE | B550M DS3H                       |            | N                             | L            | N                             | N                             |
| GIGABYTE | B660 GAMING X DDR4               |            | N                             | L            | N                             | N                             |
| GIGABYTE | B660I AORUS PRO DDR4             |            | N                             | L            | N                             | N                             |
| ASUS     | B85-PRO GAMER                    | NCT6791D   | N                             | N            | N                             | N                             |
| ASUS     | B85M-GAMER                       | NCT6791D   | N                             | N            | N                             | N                             |
| ASUS     | CROSSHAIR VI HERO                |            | Y (\AMW0._GL)                 | N            | M (\_SB.PCI0.SBRG.SIO1.MUT0)  | U (\AMW0.ASMX)                |
| ASUS     | EX-A320M-GAMING                  | IT8655E    | N                             | N            | M (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | EX-B660M-V5 D4                   |            | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | EX-B660M-V5 PRO D4               |            | N                             | N            | Y (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | EX-B760M-V5 D4                   |            | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | H170 PRO GAMING                  |            | N                             | N            | N                             | N                             |
| ASUS     | H81-GAMER                        | NCT5538D   | N                             | N            | N                             | N                             |
| ASUS     | H97-PRO GAMER                    | NCT5538D   | N                             | N            | N                             | N                             |
| ASUS     | MAXIMUS IX APEX                  |            | N                             | N            | P (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | MAXIMUS IX CODE                  | NCT6793D   | N                             | N            | P (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | MAXIMUS IX EXTREME               |            | N                             | N            | P (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | MAXIMUS IX FORMULA               | NCT6793D   | N                             | N            | P (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | MAXIMUS IX HERO                  | NCT6793D   | N                             | N            | P (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | MAXIMUS VII HERO                 | NCT6791D   | N                             | N            | P (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | P8H67                            | NCT6776F   | N                             | N            | P (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | P8Z68-V LX                       | NCT6776F   | N                             | N            | P (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | PRIME A320I-K                    | IT8655E    | N                             | N            | M (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | PRIME A320M-A                    | IT8655E    | N                             | N            | M (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | PRIME A320M-C R2.0               | IT8665E    | N                             | N            | M (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | PRIME A320M-E                    | IT8655E    | N                             | N            | M (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | PRIME A320M-F                    | IT8655E    | N                             | N            | M (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | PRIME A320M-K                    | IT8655E    | N                             | N            | M (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | PRIME A520M-A                    | NCT6798D-R | N                             | N            | U (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | PRIME A520M-A II                 | NCT6798D-R | N                             | N            | U (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | PRIME A520M-E                    | NCT6798D-R | N                             | N            | U (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | PRIME A520M-K                    | NCT6798D-R | N                             | N            | U (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B350-PLUS                  | IT8655E    | N                             | N            | M (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B350M-A                    | IT8655E    | N                             | N            | M (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B350M-E                    | IT8655E    | N                             | N            | M (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B350M-K                    | IT8655E    | N                             | N            | M (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B360-PLUS                  | NCT5582D   | N                             | N            | Y (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B360M-A                    | NCT6796D   | N                             | N            | U (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B360M-C                    | NCT6793D   | N                             | N            | U (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B360M-D                    | NCT5582D   | N                             | N            | U (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B360M-K                    | NCT5582D   | N                             | N            | U (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B450-PLUS                  | IT8665E    | N                             | N            | M (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B450M-GAMING II            | IT8655E    | N                             | N            | M (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B450M-GAMING/BR            | IT8655E    | N                             | N            | M (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B460-PLUS                  | NCT6798D   | N                             | N            | Y (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B460I-PLUS                 | NCT6798D   | N                             | N            | U (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B460M-A                    | NCT6798D   | N                             | N            | U (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B460M-A R2.0               | NCT6798D   | N                             | N            | U (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B460M-K                    | NCT6798D   | N                             | N            | U (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B550-PLUS                  | NCT6798D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B550-PLUS AC-HES           | NCT6798D-R | N                             | N            | U (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B550M-A                    | NCT6798D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B550M-A (WI-FI)            | NCT6798D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B550M-A AC                 | NCT6798D-R | N                             | N            | U (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B550M-A WIFI II            | NCT6798D-R | N                             | N            | U (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B550M-K                    | NCT6798D-R | N                             | N            | U (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B650-PLUS                  |            | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B650M-A                    |            | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B650M-A AX                 | NCT6799D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B650M-A AX II              | NCT6799D-R | N                             | N            | U (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B650M-A II                 |            | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B650M-A WIFI               |            | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B650M-A WIFI II            |            | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B660-PLUS D4               | NCT6798D   | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B660M-A AC D4              | NCT6798D   | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B660M-A D4                 |            | N                             | N            | Y (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B660M-A WIFI D4            | NCT6798D   | N                             | N            | Y (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B660M-K D4                 | NCT6798D   | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B760-PLUS D4               |            | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B760M-A AX D4              |            | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B760M-A D4                 |            | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B760M-A WIFI D4            |            | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B760M-AJ D4                |            | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | PRIME B760M-K D4                 |            | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | PRIME H410I-PLUS                 | NCT6798D   | N                             | N            | U (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | PRIME H410M-A                    |            | N                             | N            | U (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | PRIME H410M-E                    |            | N                             | N            | U (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | PRIME H410M-K                    |            | N                             | N            | U (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | PRIME H410M-K R2.0               |            | N                             | N            | U (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | PRIME H410M-R                    | NCT6798D   | N                             | N            | Y (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | PRIME X370-PRO                   | IT8665E    | N                             | N            | M (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | PRIME X399-A                     |            | N?                            | N            | N (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | PRIME X470-PRO                   | IT8665E    | Y (\AMW0._GL)                 | N            | M (\_SB.PCI0.SBRG.SIO1.MUT0)  | Y (\AMW0.ASMX)                |
| ASUS     | PRIME X570-P                     | NCT6798D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | PRIME X570-PRO                   | NCT6798D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | Y (\AMW0.ASMX)                |
| ASUS     | PRIME X670-P                     |            | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | PRIME X670-P WIFI                | NCT6799D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | PRIME X670E-PRO WIFI             | NCT6799D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | PRIME Z270-A                     | NCT6793D   | N                             | N            | P (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | PRIME Z270-K                     |            | N                             | N            | N                             | N                             |
| ASUS     | PRIME Z270-P                     |            | N                             | N            | N                             | N                             |
| ASUS     | PRIME Z270M-PLUS                 |            | N                             | N            | N                             | N                             |
| ASUS     | PRIME Z370-A                     |            | N                             | N            | N (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | PRIME Z370-A II                  |            | N                             | N            | N                             | N                             |
| ASUS     | PRIME Z590-A                     | NCT6798D   | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | PRIME Z590-P                     | NCT6798D   | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | PRIME Z590-P WIFI                | NCT6798D   | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | PRIME Z590-V                     | NCT6798D   | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | PRIME Z590M-PLUS                 | NCT6798D   | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | PRO A320M-R WI-FI                | IT8655E    | N                             | N            | M (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | PRO H410M-C                      | NCT6798D   | N                             | N            | U (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | PRO H410T                        | NCT6798D   | N                             | N            | Y (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | Pro A520M-C                      |            | N                             | N            | U (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | Pro A520M-C II                   |            | N                             | N            | U (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | Pro B550M-C                      | NCT6798D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | Pro B660M-C                      |            | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | Pro B660M-C-D4                   |            | N                             | N            | Y (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | Pro B760M-C                      |            | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | Pro B760M-CT                     |            | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | Pro WS W680-ACE                  | NCT6798D   | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | Pro WS W680-ACE IPMI             | NCT6798D   | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | Pro WS X570-ACE                  | NCT6798D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | Y (\AMW0.ASMX)                |
| ASUS     | ProArt B550-CREATOR              | NCT6798D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | U (\AMW0.ASMX)                |
| ASUS     | ProArt B650-CREATOR              |            | N                             | N            | U (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | ProArt B660-CREATOR D4           |            | N                             | N            | Y (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ProArt B760-CREATOR D4           |            | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ProArt X570-CREATOR WIFI         | NCT6798D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | Y (\AMW0.ASMX)                |
| ASUS     | ProArt X670E-CREATOR WIFI        | NCT6799D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | ProArt Z490-CREATOR 10G          | NCT6798D   | N                             | N            | Y (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ProArt Z690-CREATOR WIFI         | NCT6798D   | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ProArt Z790-CREATOR WIFI         |            | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG CROSSHAIR VI EXTREME         |            | Y (\AMW0._GL)                 | N            | M (\_SB.PCI0.SBRG.SIO1.MUT0)  | U (\AMW0.ASMX)                |
| ASUS     | ROG CROSSHAIR VI HERO (WI-FI AC) |            | Y (\AMW0._GL)                 | N            | M (\_SB.PCI0.SBRG.SIO1.MUT0)  | U (\AMW0.ASMX)                |
| ASUS     | ROG CROSSHAIR VII HERO           |            | Y (\AMW0._GL)                 | N            | M (\_SB.PCI0.SBRG.SIO1.MUT0)  | U (\AMW0.ASMX)                |
| ASUS     | ROG CROSSHAIR VII HERO (WI-FI)   |            | Y (\AMW0._GL)                 | N            | M (\_SB.PCI0.SBRG.SIO1.MUT0)  | U (\AMW0.ASMX)                |
| ASUS     | ROG CROSSHAIR VIII DARK HERO     | NCT6798D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | Y (\AMW0.ASMX)                |
| ASUS     | ROG CROSSHAIR VIII EXTREME       | NCT6798D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | U (\AMW0.ASMX)                |
| ASUS     | ROG CROSSHAIR VIII FORMULA       | NCT6798D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | Y (\AMW0.ASMX)                |
| ASUS     | ROG CROSSHAIR VIII HERO          | NCT6798D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | Y (\AMW0.ASMX)                |
| ASUS     | ROG CROSSHAIR VIII HERO (WI-FI)  | NCT6798D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | Y (\AMW0.ASMX)                |
| ASUS     | ROG CROSSHAIR VIII IMPACT        | NCT6798D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | Y (\AMW0.ASMX)                |
| ASUS     | ROG CROSSHAIR X670E EXTREME      | NCT6799D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | ROG CROSSHAIR X670E GENE         |            | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | ROG CROSSHAIR X670E HERO         | NCT6799D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | ROG MAXIMUS X HERO               | NCT6793D   | N                             | N            | P (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG MAXIMUS XI HERO              | NCT6798D   | N                             | N            | U (\_SB.PCI0.LPCB.SIO1.MUT0)  | N? (\AMW0.ASMX)               |
| ASUS     | ROG MAXIMUS XI HERO (WI-FI)      | NCT6798D   | N                             | N            | U (\_SB.PCI0.LPCB.SIO1.MUT0)  | N? (\AMW0.ASMX)               |
| ASUS     | ROG MAXIMUS XIII APEX            | NCT6798D   | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG MAXIMUS XIII EXTREME         |            | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG MAXIMUS XIII EXTREME GLACIAL |            | N                             | N            | Y (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG MAXIMUS XIII HERO            | NCT6798D   | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG MAXIMUS Z690 APEX            | NCT6798D   | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG MAXIMUS Z690 EXTREME         | NCT6798D   | N                             | N            | Y (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG MAXIMUS Z690 EXTREME GLACIAL | NCT6798D   | N                             | N            | Y (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG MAXIMUS Z690 FORMULA         | NCT6798D   | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG MAXIMUS Z690 HERO            | NCT6798D   | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG MAXIMUS Z790 EXTREME         |            | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG MAXIMUS Z790 HERO            | NCT6798D   | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX B350-F GAMING          | IT8665E    | N                             | N            | M (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX B350-I GAMING          | IT8665E    | N                             | N            | M (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX B450-E GAMING          |            | Y (\AMW0._GL)                 | N            | M (\_SB.PCI0.SBRG.SIO1.MUT0)  | U (\AMW0.ASMX)                |
| ASUS     | ROG STRIX B450-F GAMING          | IT8665E    | Y (\AMW0._GL)                 | N            | M (\_SB.PCI0.SBRG.SIO1.MUT0)  | U (\AMW0.ASMX)                |
| ASUS     | ROG STRIX B450-F GAMING II       | IT8665E    | Y (\AMW0._GL)                 | N            | M (\_SB.PCI0.SBRG.SIO1.MUT0)  | U (\AMW0.ASMX)                |
| ASUS     | ROG STRIX B450-I GAMING          |            | Y (\AMW0._GL)                 | N            | M (\_SB.PCI0.SBRG.SIO1.MUT0)  | U (\AMW0.ASMX)                |
| ASUS     | ROG STRIX B550-A GAMING          | NCT6798D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX B550-E GAMING          | NCT6798D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | Y (\AMW0.ASMX)                |
| ASUS     | ROG STRIX B550-F GAMING          | NCT6798D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX B550-F GAMING (WI-FI)  | NCT6798D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX B550-F GAMING WIFI II  | NCT6798D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX B550-I GAMING          | NCT6798D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | Y (\AMW0.ASMX)                |
| ASUS     | ROG STRIX B550-XE GAMING WIFI    | NCT6798D-R | N                             | N            | U (\_SB.PCI0.SBRG.SIO1.MUT0)  | U (\AMW0.ASMX)                |
| ASUS     | ROG STRIX B650-A GAMING WIFI     | NCT6799D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX B650E-E GAMING WIFI    | NCT6799D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX B650E-F GAMING WIFI    | NCT6799D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX B650E-I GAMING WIFI    | NCT6799D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX B660-A GAMING WIFI     | NCT6798D   | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX B660-A GAMING WIFI D4  | NCT6798D   | N                             | N            | Y (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX B660-F GAMING WIFI     | NCT6798D   | N                             | N            | Y (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX B660-G GAMING WIFI     | NCT6798D   | N                             | N            | Y (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX B660-I GAMING WIFI     | NCT6798D   | N                             | N            | Y (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX B760-A GAMING WIFI D4  |            | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX B760-F GAMING WIFI     |            | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX B760-G GAMING WIFI D4  |            | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX B760-I GAMING WIFI     |            | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX TRX40-E GAMING         | NCT6798D   | N                             | N            | P (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX TRX40-XE GAMING        | NCT6798D   | N                             | N            | P (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX X370-F GAMING          | IT8665E    | N                             | N            | M (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX X370-I GAMING          |            | N                             | N            | M (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX X399-E GAMING          |            | N?                            | N            | N (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX X470-F GAMING          | IT8665E    | Y (\AMW0._GL)                 | N            | M (\_SB.PCI0.SBRG.SIO1.MUT0)  | U (\AMW0.ASMX)                |
| ASUS     | ROG STRIX X470-I GAMING          |            | Y (\AMW0._GL)                 | N            | M (\_SB.PCI0.SBRG.SIO1.MUT0)  | U (\AMW0.ASMX)                |
| ASUS     | ROG STRIX X570-E GAMING          | NCT6798D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | Y (\AMW0.ASMX)                |
| ASUS     | ROG STRIX X570-E GAMING WIFI II  | NCT6798D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | Y (\AMW0.ASMX)                |
| ASUS     | ROG STRIX X570-F GAMING          | NCT6798D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | Y (\AMW0.ASMX)                |
| ASUS     | ROG STRIX X570-I GAMING          | NCT6798D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | Y (\AMW0.ASMX)                |
| ASUS     | ROG STRIX X670E-A GAMING WIFI    | NCT6799D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX X670E-E GAMING WIFI    | NCT6799D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX X670E-F GAMING WIFI    | NCT6799D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX X670E-I GAMING WIFI    | NCT6799D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX Z370-E GAMING          |            | N                             | N            | N                             | N                             |
| ASUS     | ROG STRIX Z370-G GAMING          |            | N                             | N            | N                             | N                             |
| ASUS     | ROG STRIX Z370-H GAMING          | NCT6793D   | N                             | N            | P (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX Z390-E GAMING          | NCT6798D   | N                             | N            | Y (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX Z390-F GAMING          | NCT6798D   | N                             | N            | Y (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX Z390-H GAMING          |            | N                             | N            | Y (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX Z390-I GAMING          |            | N                             | N            | Y (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX Z490-A GAMING          | NCT6798D   | N                             | N            | Y (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX Z490-E GAMING          | NCT6798D   | N                             | N            | Y (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX Z490-F GAMING          | NCT6798D   | N                             | N            | Y (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX Z490-G GAMING          | NCT6798D   | N                             | N            | Y (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX Z490-G GAMING (WI-FI)  | NCT6798D   | N                             | N            | Y (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX Z490-H GAMING          | NCT6798D   | N                             | N            | Y (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX Z490-I GAMING          | NCT6798D   | N                             | N            | Y (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX Z590-A GAMING WIFI     | NCT6798D   | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX Z590-A GAMING WIFI II  | NCT6798D   | N                             | N            | Y (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX Z590-E GAMING WIFI     | NCT6798D   | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX Z590-F GAMING WIFI     | NCT6798D   | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX Z590-I GAMING WIFI     | NCT6798D   | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX Z690-A GAMING WIFI D4  | NCT6798D   | N                             | N            | Y (\_SB.PC00.LPCB.SIO1.MUT0)  | N? (\RMTW.ASMX)               |
| ASUS     | ROG STRIX Z690-E GAMING WIFI     | NCT6798D   | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX Z690-F GAMING WIFI     | NCT6798D   | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG STRIX Z690-G GAMING WIFI     | NCT6798D   | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | ROG ZENITH EXTREME               |            | N?                            | N            | N                             | N                             |
| ASUS     | ROG ZENITH EXTREME ALPHA         |            | N?                            | N            | N                             | N                             |
| ASUS     | ROG ZENITH II EXTREME            | NCT6798D   | N                             | N            | P (\_SB.PCI0.SBRG.SIO1.MUT0)  | N? (\_SB_.PCI0.SBRG.SIO1.MUT0)|
| ASUS     | ROG ZENITH II EXTREME ALPHA      | NCT6798D   | N                             | N            | P (\_SB.PCI0.SBRG.SIO1.MUT0)  | N?                            |
| LENOVO   | S206                             |            | N                             | N            | N                             | N                             |
| ASUS     | STRIX Z270E-GAMING               |            | N                             | N            | P (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | STRIX Z270F-GAMING               |            | N                             | N            | P (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | STRIX Z270G-GAMING               |            | N                             | N            | P (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | STRIX Z270H-GAMING               |            | N                             | N            | P (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | STRIX Z270I-GAMING               |            | N                             | N            | N                             | N                             |
| ASUS     | TUF B350M-PLUS GAMING            | IT8655E    | N                             | N            | M (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | TUF B450-PLUS GAMING             | IT8665E    | N                             | N            | M (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | TUF GAMING A520M-PLUS            | NCT6798D-R | N                             | N            | U (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | TUF GAMING A520M-PLUS II         | NCT6798D-R | N                             | N            | U (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | TUF GAMING A520M-PLUS WIFI       | NCT6798D-R | N                             | N            | U (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | TUF GAMING B450-PLUS II          | IT8665E    | N                             | N            | M (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | TUF GAMING B550-PLUS             | NCT6798D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | TUF GAMING B550-PLUS (WI-FI)     | NCT6798D-R | N                             | N            | U (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | TUF GAMING B550-PLUS WIFI II     | NCT6798D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | TUF GAMING B550-PRO              | NCT6798D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | TUF GAMING B550M-E               | NCT6798D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | TUF GAMING B550M-E WIFI          | NCT6798D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | TUF GAMING B550M-PLUS            | NCT6798D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | TUF GAMING B550M-PLUS (WI-FI)    | NCT6798D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | TUF GAMING B550M-PLUS WIFI II    | NCT6798D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | TUF GAMING B650-PLUS             |            | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | TUF GAMING B650-PLUS WIFI        | NCT6799D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | TUF GAMING B650M-PLUS            | NCT6799D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | TUF GAMING B650M-PLUS WIFI       | NCT6799D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | TUF GAMING B660-PLUS WIFI D4     | NCT6798D   | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | TUF GAMING B660M-E D4            | NCT6798D   | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | TUF GAMING B660M-PLUS D4         | NCT6798D   | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | TUF GAMING B660M-PLUS WIFI       | NCT6798D   | N                             | N            | Y (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | TUF GAMING B660M-PLUS WIFI D4    | NCT6798D   | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | TUF GAMING B760-PLUS WIFI D4     |            | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | TUF GAMING B760M-PLUS D4         |            | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | TUF GAMING B760M-PLUS WIFI D4    |            | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | TUF GAMING X570-PLUS             | NCT6798D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | TUF GAMING X570-PLUS (WI-FI)     | NCT6798D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | TUF GAMING X570-PLUS_BR          | NCT6798D-R | N                             | N            | U (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | TUF GAMING X570-PRO (WI-FI)      | NCT6798D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | TUF GAMING X570-PRO WIFI II      | NCT6798D-R | N                             | N            | U (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | TUF GAMING X670E-PLUS            |            | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | TUF GAMING X670E-PLUS WIFI       | NCT6799D-R | N                             | N            | Y (\_SB.PCI0.SBRG.SIO1.MUT0)  | N                             |
| ASUS     | TUF GAMING Z490-PLUS             | NCT6798D   | N                             | N            | Y (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | TUF GAMING Z490-PLUS (WI-FI)     | NCT6798D   | N                             | N            | Y (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | TUF GAMING Z590-PLUS             | NCT6798D   | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | TUF GAMING Z590-PLUS WIFI        | NCT6798D   | N                             | N            | Y (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | TUF Z270 MARK 1                  | NCT6793D   | N                             | N            | P (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| GIGABYTE | X570 AORUS ELITE                 |            | N                             | Y            | N                             | N                             |
| GIGABYTE | X570 AORUS ELITE WIFI            | IT8688E    | N                             | Y            | N                             | N                             |
| GIGABYTE | X570 GAMING X                    |            | N                             | L            | N                             | N                             |
| GIGABYTE | X570 I AORUS PRO WIFI            | IT8688E    | N                             | Y            | N                             | N                             |
| GIGABYTE | X570 UD                          |            | N                             | L            | N                             | N                             |
| ASUS     | X99-E WS/USB 3.1                 |            | N                             | N            | L (\_SB_.PCI0.LPC0.SIO1.MUT0) | N                             |
| ASUS     | X99-E-10G WS                     |            | N                             | N            | N                             | N                             |
| ASUS     | Z170 PRO GAMING                  | NCT6793D   | N                             | N            | P (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | Z170 PRO GAMING/AURA             | NCT6793D   | N                             | N            | P (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | Z170-DELUXE                      | NCT6793D   | N                             | N            | P (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | Z170I PRO GAMING                 | NCT5539D   | N                             | N            | P (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | Z170M-PLUS                       | NCT6793D   | N                             | N            | P (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| ASUS     | Z270-WS                          |            | N                             | N            | P (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| GIGABYTE | Z390 I AORUS PRO WIFI-CF         |            | N                             | L            | N                             | N                             |
| GIGABYTE | Z490 AORUS ELITE AC              |            | N                             | L            | N                             | N                             |
| ASUS     | Z490-GUNDAM (WI-FI)              |            | N                             | N            | U (\_SB.PCI0.LPCB.SIO1.MUT0)  | N                             |
| GIGABYTE | Z590 AORUS ELITE AX              |            | N                             | N            | L                             | N                             |
| GIGABYTE | Z590 AORUS MASTER                |            | N                             | N            | L                             | N                             |
| GIGABYTE | Z590 AORUS PRO AX                |            | N                             | N            | L                             | N                             |
| GIGABYTE | Z590 AORUS ULTRA                 |            | N                             | N            | L                             | N                             |
| GIGABYTE | Z590 D                           |            | N                             | N            | L                             | N                             |
| GIGABYTE | Z590 GAMING X                    |            | N                             | N            | L                             | N                             |
| GIGABYTE | Z590 UD                          |            | N                             | N            | L                             | N                             |
| GIGABYTE | Z590 UD AC                       |            | N                             | N            | L                             | N                             |
| GIGABYTE | Z590 VISION D                    |            | N                             | N            | L                             | N                             |
| GIGABYTE | Z590 VISION G                    |            | N                             | N            | L                             | N                             |
| ASUS     | Z590 WIFI GUNDAM EDITION         | NCT6798D   | N                             | N            | U (\_SB.PC00.LPCB.SIO1.MUT0)  | N                             |
| GIGABYTE | Z590I AORUS ULTRA                |            | N                             | N            | L                             | N                             |
| GIGABYTE | Z590I VISION D                   |            | N                             | N            | L                             | N                             |
| GIGABYTE | Z590M                            |            | N                             | N            | L                             | N                             |
| GIGABYTE | Z590M GAMING X                   |            | N                             | N            | L                             | N                             |
| GIGABYTE | Z690M AORUS ELITE AX DDR4        |            | N                             | Y            | N                             | N                             |
| ASUS     | Z97-PRO GAMER                    | NCT5538D   | N                             | N            | N                             | N                             |

* L - no DSDL/SSDL dumps,
* N - unsupported,
* Y - supported and upstreamed,
* U - to upstream,
* ? - upstreamed but not detected by script,
* M - required method exists, port defined in different way,
* W - required method exists, no wmi method defined,
* P - return zero, no valid sensors results or requires custom lock.

# Entry point definition

For monitoring GUID: "466747A0-70EC-11DE-8A39-0800200C9A66"

```
    Name (_HID, EisaId ("PNP0C14") /* Windows Management Instrumentation Device */)  // _HID: Hardware ID
    Name (_UID, "ASUSWMI")  // _UID: Unique ID
    Name (_WDG, Buffer (0x50)
    {
        /* 0000 */  0xD0, 0x5E, 0x84, 0x97, 0x6D, 0x4E, 0xDE, 0x11,  // .^..mN..
        /* 0008 */  0x8A, 0x39, 0x08, 0x00, 0x20, 0x0C, 0x9A, 0x66,  // .9.. ..f
        /* 0010 */  0x42, 0x43, 0x01, 0x02, 0xA0, 0x47, 0x67, 0x46,  // BC...GgF
        /* 0018 */  0xEC, 0x70, 0xDE, 0x11, 0x8A, 0x39, 0x08, 0x00,  // .p...9..
        /* 0020 */  0x20, 0x0C, 0x9A, 0x66, 0x42, 0x44, 0x01, 0x02,  //  ..fBD..
        /* 0028 */  0x72, 0x0F, 0xBC, 0xAB, 0xA1, 0x8E, 0xD1, 0x11,  // r.......
        /* 0030 */  0x00, 0xA0, 0xC9, 0x06, 0x29, 0x10, 0x00, 0x00,  // ....)...
        /* 0038 */  0xD2, 0x00, 0x01, 0x08, 0x21, 0x12, 0x90, 0x05,  // ....!...
        /* 0040 */  0x66, 0xD5, 0xD1, 0x11, 0xB2, 0xF0, 0x00, 0xA0,  // f.......
        /* 0048 */  0xC9, 0x06, 0x29, 0x10, 0x4D, 0x4F, 0x01, 0x00   // ..).MO..
    })
```

# Port definition
```
    Name (IOHW, 0x0290)

    OperationRegion (SHWM, SystemIO, IOHW, 0x0A)
    Field (SHWM, ByteAcc, NoLock, Preserve)
    {
        Offset (0x05),
        HIDX,   8,
        HDAT,   8
    }
```
# Required code samples for nct6775 support (`ROG STRIX B550-E GAMING` based)

## Hex to Function name

```
    Case (0x5253494F)
    {
        Return (RSIO (Arg2))
    }
    Case (0x5753494F)
    {
        Return (WSIO (Arg2))
    }
    Case (0x5248574D)
    {
        Return (RHWM (Arg2))
    }
    Case (0x5748574D)
    {
        Return (WHWM (Arg2))
    }
```

## IO Functions

```
    Method (RSIO, 1, Serialized)
    {
        If ((Acquire (ASMX, 0xFFFF) == Zero))
        {
            CreateByteField (Arg0, Zero, W_LN)
            CreateByteField (Arg0, One, W_ID)
            Local0 = Ones
            If ((Acquire (\_SB.PCI0.SBRG.SIO1.MUT0, 0xFFFF) == Zero))
            {
                \_SB.PCI0.SBRG.SIO1.ENFG (W_LN)
                \_SB.PCI0.SBRG.SIO1.INDX = W_ID /* \AMW0.RSIO.W_ID */
                Local0 = \_SB.PCI0.SBRG.SIO1.DATA
                \_SB.PCI0.SBRG.SIO1.EXFG ()
            }

            Release (ASMX)
            Return (Local0)
        }

        Return (Ones)
    }

    Method (WSIO, 1, Serialized)
    {
        If ((Acquire (ASMX, 0xFFFF) == Zero))
        {
            CreateByteField (Arg0, Zero, W_LN)
            CreateByteField (Arg0, One, W_ID)
            CreateByteField (Arg0, 0x02, W_DT)
            Local0 = Ones
            If ((Acquire (\_SB.PCI0.SBRG.SIO1.MUT0, 0xFFFF) == Zero))
            {
                \_SB.PCI0.SBRG.SIO1.ENFG (W_LN)
                \_SB.PCI0.SBRG.SIO1.INDX = W_ID /* \AMW0.WSIO.W_ID */
                \_SB.PCI0.SBRG.SIO1.DATA = W_DT /* \AMW0.WSIO.W_DT */
                \_SB.PCI0.SBRG.SIO1.EXFG ()
            }

            Release (ASMX)
            Return (Local0)
        }

        Return (Ones)
    }
```

## WM Functions

```
    Method (RHWM, 1, Serialized)
    {
        If ((Acquire (ASMX, 0xFFFF) == Zero))
        {
            CreateByteField (Arg0, Zero, W_BK)
            CreateByteField (Arg0, One, W_ID)
            \_SB.PCI0.SBRG.SIO1.ENFG (0x07)
            LCKS = HMLK /* \AMW0.HMLK */
            HMLK = Zero
            BANK = W_BK /* \AMW0.RHWM.W_BK */
            HIDX = W_ID /* \AMW0.RHWM.W_ID */
            Local0 = HDAT /* \AMW0.HDAT */
            HMLK = LCKS /* \AMW0.LCKS */
            \_SB.PCI0.SBRG.SIO1.EXFG ()
            Release (ASMX)
            Return (Local0)
        }

        Return (Ones)
    }

    Method (WHWM, 1, Serialized)
    {
        If ((Acquire (ASMX, 0xFFFF) == Zero))
        {
            CreateByteField (Arg0, Zero, W_BK)
            CreateByteField (Arg0, One, W_ID)
            CreateByteField (Arg0, 0x02, W_DT)
            \_SB.PCI0.SBRG.SIO1.ENFG (0x07)
            LCKS = HMLK /* \AMW0.HMLK */
            HMLK = Zero
            BANK = W_BK /* \AMW0.WHWM.W_BK */
            HIDX = W_ID /* \AMW0.WHWM.W_ID */
            HDAT = W_DT /* \AMW0.WHWM.W_DT */
            HMLK = LCKS /* \AMW0.LCKS */
            \_SB.PCI0.SBRG.SIO1.EXFG ()
            Release (ASMX)
            Return (Zero)
        }

        Return (Ones)
    }
```

# Required code samples for asus_wmi_sensors boards support (`ROG-STRIX-B450-E-GAMING` based)

## Hex to Function name

```
    Case (0x52574543)
    {
        Return (RSEN (Arg2))
    }
    Case (0x51574543)
    {
        Return (UPSB (Arg2))
    }
    Case (0x50574543)
    {
        Return (GNAM (Arg2))
    }
    Case (0x50574572)
    {
        Return (GNUM (Arg2))
    }
    Case (0x50574574)
    {
        Return (GVER (Arg2))
    }
```

## Functions

```
    Method (RSEN, 1, Serialized)
    {
        CreateByteField (Arg0, Zero, INDX)
        If ((INDX == Zero))
        {
            Local0 = NU00 /* \AMW0.NU00 */
        }
        ElseIf ((INDX == One))
        {
            Local0 = NU01 /* \AMW0.NU01 */
        }
        ElseIf ((INDX == 0x02))
        {
            Local0 = NU02 /* \AMW0.NU02 */
        }
        ElseIf ((INDX == 0x03))
        {
            Local0 = NU03 /* \AMW0.NU03 */
        }
        ElseIf ((INDX == 0x04))
        {
            Local0 = NU04 /* \AMW0.NU04 */
        }
        ElseIf ((INDX == 0x05))
        {
            Local0 = NU05 /* \AMW0.NU05 */
        }
        ElseIf ((INDX == 0x06))
        {
            Local0 = NU06 /* \AMW0.NU06 */
        }
        ElseIf ((INDX == 0x07))
        {
            Local0 = NU07 /* \AMW0.NU07 */
        }
        ElseIf ((INDX == 0x08))
        {
            Local0 = NU08 /* \AMW0.NU08 */
        }
        ElseIf ((INDX == 0x09))
        {
            Local0 = NU09 /* \AMW0.NU09 */
        }
        ElseIf ((INDX == 0x0A))
        {
            Local0 = NU10 /* \AMW0.NU10 */
        }
        ElseIf ((INDX == 0x0B))
        {
            Local0 = NU11 /* \AMW0.NU11 */
        }
        ElseIf ((INDX == 0x0C))
        {
            Local0 = NU12 /* \AMW0.NU12 */
        }
        ElseIf ((INDX == 0x0D))
        {
            Local0 = NU13 /* \AMW0.NU13 */
        }
        ElseIf ((INDX == 0x0E))
        {
            Local0 = NU14 /* \AMW0.NU14 */
        }
        ElseIf ((INDX == 0x0F))
        {
            Local0 = NU15 /* \AMW0.NU15 */
        }
        ElseIf ((INDX == 0x10))
        {
            Local0 = NU16 /* \AMW0.NU16 */
        }
        ElseIf ((INDX == 0x11))
        {
            Local0 = NU17 /* \AMW0.NU17 */
        }
        ElseIf ((INDX == 0x12))
        {
            Local0 = NU18 /* \AMW0.NU18 */
        }
        ElseIf ((INDX == 0x13))
        {
            Local0 = NU19 /* \AMW0.NU19 */
        }
        ElseIf ((INDX == 0x14))
        {
            Local0 = NU20 /* \AMW0.NU20 */
        }
        ElseIf ((INDX == 0x15))
        {
            Local0 = NU21 /* \AMW0.NU21 */
        }
        ElseIf ((INDX == 0x16))
        {
            Local0 = NU22 /* \AMW0.NU22 */
        }
        ElseIf ((INDX == 0x17))
        {
            Local0 = NU23 /* \AMW0.NU23 */
        }
        Else
        {
            Local0 = Zero
        }

        Return (Local0)
    }

    Method (GNAM, 1, Serialized)
    {
        CreateByteField (Arg0, Zero, _NUM)
        Local0 = DerefOf (DerefOf (INFO [Arg0]) [Zero])
        RETN [Zero] = Local0
        Local0 = DerefOf (DerefOf (INFO [Arg0]) [One])
        RETN [One] = Local0
        Local0 = DerefOf (DerefOf (INFO [Arg0]) [0x02])
        RETN [0x02] = Local0
        Local0 = DerefOf (DerefOf (INFO [Arg0]) [0x03])
        RETN [0x03] = Local0
        Local0 = DerefOf (DerefOf (INFO [Arg0]) [0x04])
        RETN [0x04] = Local0
        Return (RETN) /* \AMW0.RETN */
    }

    Method (GNUM, 1, Serialized)
    {
        Local0 = SizeOf (INFO)
        Return (Local0)
    }

    Method (UPSB, 1, Serialized)
    {
        CreateByteField (Arg0, Zero, UPDS)
        If ((UPDS == Zero))
        {
            Local0 = UPEC ()
            Local0 = UPHM ()
        }
        ElseIf ((UPDS == One))
        {
            Local0 = UPHM ()
        }
        ElseIf ((UPDS == 0x02))
        {
            Local0 = UPEC ()
        }
        Else
        {
            Return (Ones)
        }

        Return (Local0)
    }

    Name (VERN, 0x03)
    Method (GVER, 1, Serialized)
    {
        Return (VERN) /* \AMW0.VERN */
    }
```

# Required code samples for asus_ec_sensors boards support (`ROG STRIX X570-E GAMING` based)

## Hex to Function name

```
    Case (0x42524543)
    {
        Return (BREC (Arg2))
    }
```

## IO Functions

```
    Method (BREC, 1, Serialized)
    {
        CreateByteField (Arg0, Zero, WLEN)
        B_CT = (WLEN >> 0x02)
        If ((B_CT > 0x20))
        {
            Return (Ones)
        }

        If ((Acquire (ASMX, 0xFFFF) == Zero))
        {
            IDBF = STOH (Arg0)
            Local0 = Zero
            Local1 = Zero
            While ((Local0 < B_CT))
            {
                B_BK = DerefOf (IDBF [Local0])
                Local0++
                B_ID = DerefOf (IDBF [Local0])
                Local0++
                ECBK = \_SB.PCI0.SBRG.EC0.EBFF
                \_SB.PCI0.SBRG.EC0.EBFF = B_BK /* \AMW0.B_BK */
                ODBF [Local1] = \_SB.PCI0.SBRG.EC0.ECCM (B_ID, Zero, Zero)
                \_SB.PCI0.SBRG.EC0.EBFF = ECBK /* \AMW0.ECBK */
                Local1++
            }

            OSBF = HTOS (ODBF, Local1)
            Release (ASMX)
            Return (OSBF) /* \AMW0.OSBF */
        }

        Return (Ones)
    }
```

# Additional info

## _WDG Format

From [WMI](https://wiki.ubuntu.com/FirmwareTestSuite/Reference/wmi)
and [fwts](https://git.launchpad.net/fwts).

```
typedef struct {
    uint8_t    guid[16];            /* GUID */
    union {
        uint8_t     obj_id[2];    /* Object Identifier */
        struct {
            uint8_t    notify_id;    /* Notify Identifier */
            uint8_t    reserved;    /* Reserved */
        } notify;
    } id;
    uint8_t    instance;            /* Instance */
    uint8_t    flags;                /* fwts_wmi_flags */
} __attribute__ ((packed)) fwts_wdg_info;
```

## Steps for add your board to list

 * Check that your board is not metntioned in [bug report](https://bugzilla.kernel.org/show_bug.cgi?id=204807)
 * Check that sensor is appear when added `acpi_enforce_resources=lax` to boot params.
 * If sensor appear, send such as attachment to buf report:
    * your motherboard name (/sys/class/dmi/id/board_name)
    * dsdt uefi dump "acpidump -b -n DSDT"
    * What error do you have in dmesg near `nct6775`?

## kernel build

Install without package manager and default config
```shell
make defconfig
make -j 2
sudo make modules_install
sudo make install
```

Install with deb package manager and current config
```shell
# copy current config
cp /boot/config-`uname -r` .config
# build
make oldconfig
make -j 2
make CC="ccache gcc" bindeb-pkg
# install packages
sudo dpk -i *.deb
```

Or look to official documentation:
 * [Debian](https://wiki.debian.org/BuildADebianKernelPackage)
 * [Ubuntu](https://wiki.ubuntu.com/Kernel/BuildYourOwnKernel)
 * [Fedora](https://fedoraproject.org/wiki/Building_a_custom_kernel)
 * [Archlinux](https://wiki.archlinux.org/title/Kernel/Traditional_compilation)
