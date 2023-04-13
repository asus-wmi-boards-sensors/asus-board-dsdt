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
* [ASUS nct6775 upstream](https://git.kernel.org/pub/scm/linux/kernel/git/groeck/linux-staging.git/tree/drivers/hwmon/nct6775-platform.c?h=hwmon-next)
* [ASUS wmi upstream](https://git.kernel.org/pub/scm/linux/kernel/git/groeck/linux-staging.git/tree/drivers/hwmon/asus_wmi_sensors.c?h=hwmon-next)
* [Gigabyte](https://github.com/t-8ch/linux-gigabyte-wmi-driver)
* [Gigabyte wmi upstream](https://git.kernel.org/pub/scm/linux/kernel/git/groeck/linux-staging.git/tree/drivers/platform/x86/gigabyte-wmi.c?h=hwmon-next)
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

# TODO

Port to use asl directly instead disassembling to dsl.

# Supported boards

| made by  | board name                          | superio    | asus-wmi     | gigabyte-wmi | nct6775      | asus-ec      |
| ---------| ----------------------------------- | ---------- | ------------ | ------------ | ------------ | ------------ |
| ASUS     | 970 PRO GAMING/AURA                 |            | F            | N            | F            | N            |
| GIGABYTE | 970A-DS3P                           |            | N            | N            | N            | N            |
| GIGABYTE | 990XA-UD3                           |            | N            | N            | N            | N            |
| ASUS     | A320M-C                             | IT8665E    | N            | N            | P            | N            |
| GIGABYTE | A320M-S2H-CF                        |            | N            | U            | N            | N            |
| ASUS     | A68HM-K                             |            | N            | N            | N            | N            |
| ASUS     | A68HM-PLUS                          |            | N            | N            | N            | N            |
| ASUS     | A88X-GAMER                          |            | F            | N            | F            | N            |
| ASUS     | B150 PRO GAMING                     | NCT6793D   | N            | N            | P            | N            |
| ASUS     | B150 PRO GAMING D3                  | NCT6793D   | N            | N            | P            | N            |
| ASUS     | B150 PRO GAMING/AURA                | NCT6793D   | F            | N            | F            | N            |
| ASUS     | B150I PRO GAMING/AURA               | NCT5539D   | N            | N            | P            | N            |
| ASUS     | B150I PRO GAMING/WIFI/AURA          | NCT5539D   | N            | N            | P            | N            |
| ASUS     | B150M PRO GAMING                    | NCT6793D   | N            | N            | P            | N            |
| ASUS     | B250 MINING EXPERT                  | NCT5539D   | N            | N            | P            | N            |
| ASUS     | B250M-C PRO                         | NCT5539D   | N            | N            | P            | N            |
| ASUS     | B360M-BASALT                        | NCT5582D   | N            | N            | Y            | N            |
| ASUS     | B360M-D3H                           | NCT5582D   | N            | N            | Y            | N            |
| ASROCK   | B365M Pro4-F                        |            | N            | N            | P            | N            |
| GIGABYTE | B450 AORUS ELITE                    |            | N            | U            | N            | N            |
| GIGABYTE | B450 AORUS PRO WIFI-CF              |            | N            | U            | N            | N            |
| GIGABYTE | B450M DS3H V2                       |            | N            | U            | N            | N            |
| GIGABYTE | B450M DS3H WIFI-CF                  |            | N            | Y            | N            | N            |
| GIGABYTE | B450M DS3H-CF                       |            | N            | Y            | N            | N            |
| ASROCK   | B450M Pro4                          |            | N            | N            | P            | N            |
| GIGABYTE | B450M S2H V2                        |            | N            | Y            | N            | N            |
| ASUS     | B450M-DRAGON                        | IT8655E    | N            | N            | M            | N            |
| GIGABYTE | B550 AORUS ELITE                    |            | N            | Y            | N            | N            |
| GIGABYTE | B550 AORUS ELITE AX V2              |            | N            | Y            | N            | N            |
| GIGABYTE | B550 AORUS ELITE V2                 |            | N            | Y            | N            | N            |
| GIGABYTE | B550 AORUS PRO V2                   |            | N            | U            | N            | N            |
| GIGABYTE | B550 GAMING X V2                    |            | N            | Y            | N            | N            |
| GIGABYTE | B550I AORUS PRO AX                  |            | N            | Y            | N            | N            |
| GIGABYTE | B550M AORUS PRO-P                   |            | N            | Y            | N            | N            |
| GIGABYTE | B550M DS3H                          |            | N            | Y            | N            | N            |
| ASUS     | B560M-A PRIME                       |            | L            | N            | L            | N            |
| ASUS     | B560M-P                             | NCT6798D   | N            | N            | Y            | N            |
| ASROCK   | B650E PG Riptide WiFi               |            | N            | N            | P            | N            |
| GIGABYTE | B660 GAMING X DDR4                  |            | N            | Y            | N            | N            |
| GIGABYTE | B660I AORUS PRO DDR4                |            | N            | Y            | N            | N            |
| ASUS     | B85-PRO GAMER                       | NCT6791D   | N            | N            | N            | N            |
| ASUS     | B85M-GAMER                          | NCT6791D   | N            | N            | N            | N            |
| ASUS     | CROSSHAIR VI HERO                   | IT8655E    | Y            | N            | M            | U            |
| ASUS     | EX-A320M-GAMING                     | IT8655E    | N            | N            | M            | N            |
| ASUS     | EX-B360M-V                          | NCT5582D   | N            | N            | Y            | N            |
| ASUS     | EX-B360M-V3                         | NCT5582D   | N            | N            | Y            | N            |
| ASUS     | EX-B360M-V5                         | NCT5582D   | N            | N            | Y            | N            |
| ASUS     | EX-B365M-V                          | NCT5582D   | N            | N            | P            | N            |
| ASUS     | EX-B365M-V5                         | NCT5582D   | N            | N            | P            | N            |
| ASUS     | EX-B460M-V5                         | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | EX-B560M-V5                         | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | EX-B660M-V5 D4                      | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | EX-B660M-V5 PRO D4                  | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | EX-B760M-V5 D4                      | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | EX-H310M-V3 R2.0                    | NCT5582D   | N            | N            | P            | N            |
| ASUS     | EX-H410M-V3                         | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | EX-H510M-V3                         | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | EX-H610M-V3 D4                      | NCT6798D   | N            | N            | Y            | N            |
| GIGABYTE | EX58-UD5                            |            | N            | N            | N            | N            |
| GIGABYTE | F2A78M-HD2                          |            | N            | N            | N            | N            |
| ASUS     | FX570UD                             |            | L            | N            | L            | N            |
| GIGABYTE | GA-MA78LMT-US2H                     |            | N            | N            | N            | N            |
| ASUS     | H110-PLUS                           | NCT6793D   | L            | N            | L            | N            |
| ASUS     | H110I-PLUS                          | NCT5539D   | L            | N            | L            | N            |
| ASUS     | H110M-A                             | NCT5539D   | L            | N            | L            | N            |
| ASUS     | H110M-A D3                          | NCT5539D   | L            | N            | L            | N            |
| ASUS     | H110M-A/DP                          | NCT5539D   | L            | N            | L            | N            |
| ASUS     | H110M-A/M.2                         | NCT5539D   | N            | N            | P            | N            |
| ASUS     | H110M-C                             | NCT6791D   | L            | N            | L            | N            |
| ASUS     | H110M-C/BR                          | NCT6791D   | L            | N            | L            | N            |
| ASUS     | H110M-C/PS                          | NCT6791D   | L            | N            | L            | N            |
| ASUS     | H110M-C2                            | NCT6791D   | L            | N            | L            | N            |
| ASUS     | H110M-CS                            | NCT6791D   | L            | N            | L            | N            |
| ASUS     | H110M-CS/BR                         | NCT6791D   | L            | N            | L            | N            |
| ASUS     | H110M-D                             | NCT6793D   | L            | N            | L            | N            |
| ASUS     | H110M-E                             | NCT5539D   | L            | N            | L            | N            |
| ASUS     | H110M-E-M.2                         | NCT5539D   | L            | N            | L            | N            |
| ASUS     | H110M-E/M.2                         | NCT5539D   | L            | N            | L            | N            |
| ASUS     | H110M-F                             | NCT5539D   | L            | N            | L            | N            |
| ASUS     | H110M-K                             | NCT5539D   | L            | N            | L            | N            |
| ASUS     | H110M-K D3                          | NCT5539D   | L            | N            | L            | N            |
| ASUS     | H110M-PLUS                          | NCT5539D   | L            | N            | L            | N            |
| ASUS     | H110M-R                             | NCT6791D   | L            | N            | L            | N            |
| ASUS     | H110S1                              | NCT5539D   | L            | N            | L            | N            |
| ASUS     | H110S2                              | NCT5539D   | L            | N            | L            | N            |
| ASUS     | H110T                               | NCT5539D   | L            | N            | L            | N            |
| ASUS     | H170 PRO GAMING                     | NCT6793D   | F            | N            | F            | N            |
| ASUS     | H61M-A                              | NCT5535D   | L            | N            | L            | N            |
| ASUS     | H61M-A/BR                           | NCT5535D   | L            | N            | L            | N            |
| ASUS     | H61M-A/USB3                         | NCT5535D   | L            | N            | L            | N            |
| ASUS     | H61M-C                              | NCT5535D   | L            | N            | L            | N            |
| ASUS     | H61M-CS                             | NCT5535D   | L            | N            | L            | N            |
| ASUS     | H61M-D                              | NCT5535D   | L            | N            | L            | N            |
| ASUS     | H61M-E                              | IT8603E    | L            | N            | L            | N            |
| ASUS     | H61M-F                              | NCT5535D   | L            | N            | L            | N            |
| ASUS     | H61M-K                              | NCT5535D   | L            | N            | L            | N            |
| ASUS     | H61M-PLUS                           | NCT5535D   | L            | N            | L            | N            |
| ASUS     | H61M-PRO                            | NCT5535D   | L            | N            | L            | N            |
| ASROCK   | H77M                                |            | N            | N            | N            | N            |
| ASUS     | H81-GAMER                           | NCT5538D   | N            | N            | N            | N            |
| ASUS     | H81-PLUS                            | NCT6791D   | L            | N            | L            | N            |
| ASUS     | H81I-PLUS                           | NCT5535D2  | L            | N            | L            | N            |
| ASUS     | H81M-A                              | NCT5538D   | L            | N            | L            | N            |
| ASUS     | H81M-A/BR                           | NCT5538D   | L            | N            | L            | N            |
| ASUS     | H81M-C                              | NCT6791D   | L            | N            | L            | N            |
| ASUS     | H81M-C/BR                           | NCT6791D   | L            | N            | L            | N            |
| ASUS     | H81M-CS                             | NCT5538D   | L            | N            | L            | N            |
| ASUS     | H81M-CS/BR                          | NCT5538D   | L            | N            | L            | N            |
| ASUS     | H81M-D                              | NCT5538D   | L            | N            | L            | N            |
| ASUS     | H81M-D PLUS                         | NCT5538D   | L            | N            | L            | N            |
| ASUS     | H81M-E                              | NCT5538D   | L            | N            | L            | N            |
| ASUS     | H81M-K                              | NCT5538D   | L            | N            | L            | N            |
| ASUS     | H81M-P                              | NCT5538D   | L            | N            | L            | N            |
| ASUS     | H81M-P PLUS                         | NCT5535D   | L            | N            | L            | N            |
| ASUS     | H81M-PLUS                           | NCT5538D   | L            | N            | L            | N            |
| ASUS     | H81M-R                              | NCT5538D   | N            | N            | P            | N            |
| ASUS     | H81M-V3                             | NCT6791D   | L            | N            | L            | N            |
| ASUS     | H81M2                               | NCT6791D   | L            | N            | L            | N            |
| ASUS     | H81T                                | NCT6791D   | L            | N            | L            | N            |
| ASUS     | H97-PRO GAMER                       | NCT5538D   | N            | N            | N            | N            |
| ASUS     | K30AD_M31AD_M51AD_M32AD             | NCT5538D   | N            | N            | P            | N            |
| ASUS     | M4A88TD-V EVO/USB3                  |            | N            | N            | N            | N            |
| ASUS     | M5A78L-M PLUS/USB3                  | IT8728F    | N            | N            | N            | N            |
| ASUS     | M5A88-M                             |            | N            | N            | N            | N            |
| ASUS     | MAXIMUS IX APEX                     | NCT6793D   | N            | N            | P            | N            |
| ASUS     | MAXIMUS IX CODE                     | NCT6793D   | N            | N            | P            | N            |
| ASUS     | MAXIMUS IX EXTREME                  | NCT6793D   | N            | N            | P            | N            |
| ASUS     | MAXIMUS IX FORMULA                  | NCT6793D   | N            | N            | P            | N            |
| ASUS     | MAXIMUS IX HERO                     | NCT6793D   | N            | N            | P            | N            |
| ASUS     | MAXIMUS VII HERO                    | NCT6791D   | N            | N            | P            | N            |
| ASUS     | MAXIMUS VIII FORMULA                | NCT6793D   | N            | N            | P            | N            |
| ASUS     | P5GC-MX                             |            | N            | N            | P            | N            |
| ASUS     | P5Q-EM                              |            | N            | N            | P            | N            |
| ASUS     | P5QL PRO                            |            | N            | N            | P            | N            |
| ASUS     | P5VD2-VM                            |            | N            | N            | N            | N            |
| ASUS     | P8H61                               | NCT6779D   | L            | N            | L            | N            |
| ASUS     | P8H61 PLUS                          | NCT6776F   | L            | N            | L            | N            |
| ASUS     | P8H61 PRO                           | NCT6779D   | L            | N            | L            | N            |
| ASUS     | P8H61 R2.0                          | NCT6779D   | L            | N            | L            | N            |
| ASUS     | P8H61-I                             | NCT6779D   | L            | N            | L            | N            |
| ASUS     | P8H61-I LX                          | NCT5579D   | L            | N            | L            | N            |
| ASUS     | P8H61-I LX R2.0                     | NCT5535D   | L            | N            | L            | N            |
| ASUS     | P8H61-I LX R2.0/RM/SI               | NCT5535D   | L            | N            | L            | N            |
| ASUS     | P8H61-I R2.0                        | NCT5579D   | L            | N            | L            | N            |
| ASUS     | P8H61-M                             | NCT6776F   | L            | N            | L            | N            |
| ASUS     | P8H61-M EVO                         | NCT6776F   | L            | N            | L            | N            |
| ASUS     | P8H61-M LE                          | NCT6779D   | L            | N            | L            | N            |
| ASUS     | P8H61-M LE R2.0                     | NCT6779D   | L            | N            | L            | N            |
| ASUS     | P8H61-M LE/BR                       | NCT6776F   | L            | N            | L            | N            |
| ASUS     | P8H61-M LE/CSM                      | NCT6776F   | L            | N            | L            | N            |
| ASUS     | P8H61-M LE/CSM R2.0                 | NCT6779D   | L            | N            | L            | N            |
| ASUS     | P8H61-M LE/USB3                     | NCT6776F   | L            | N            | L            | N            |
| ASUS     | P8H61-M LX                          | NCT6779D   | L            | N            | L            | N            |
| ASUS     | P8H61-M LX PLUS                     | NCT6776F   | L            | N            | L            | N            |
| ASUS     | P8H61-M LX PLUS R2.0                | NCT6779D   | L            | N            | L            | N            |
| ASUS     | P8H61-M LX R2.0                     | NCT6779D   | N            | N            | P            | N            |
| ASUS     | P8H61-M LX2                         | NCT6779D   | L            | N            | L            | N            |
| ASUS     | P8H61-M LX2 2.0                     | NCT5535D   | L            | N            | L            | N            |
| ASUS     | P8H61-M LX2 R2.0                    | NCT5535D   | L            | N            | L            | N            |
| ASUS     | P8H61-M LX2/CSM                     | NCT6779D   | L            | N            | L            | N            |
| ASUS     | P8H61-M LX3                         | NCT6779D   | L            | N            | L            | N            |
| ASUS     | P8H61-M LX3 PLUS                    | NCT6779D   | L            | N            | L            | N            |
| ASUS     | P8H61-M LX3 PLUS R2.0               | NCT5535D   | L            | N            | L            | N            |
| ASUS     | P8H61-M LX3 R2.0                    | NCT5535D   | L            | N            | L            | N            |
| ASUS     | P8H61-M PLUS V2                     | NCT6779D   | L            | N            | L            | N            |
| ASUS     | P8H61-M PRO                         | NCT6776F   | L            | N            | L            | N            |
| ASUS     | P8H61-M2 USB3                       | NCT6779D   | L            | N            | L            | N            |
| ASUS     | P8H61-M2/SI                         | NCT6779D   | L            | N            | L            | N            |
| ASUS     | P8H61-MX                            | NCT6779D   | L            | N            | L            | N            |
| ASUS     | P8H61-MX R2.0                       | NCT5535D   | L            | N            | L            | N            |
| ASUS     | P8H61-MX USB3                       | NCT5535D   | L            | N            | L            | N            |
| ASUS     | P8H61-V                             | NCT6776F   | L            | N            | L            | N            |
| ASUS     | P8H61/USB3                          | NCT6779D   | L            | N            | L            | N            |
| ASUS     | P8H61/USB3 R2.0                     | NCT6779D   | L            | N            | L            | N            |
| ASUS     | P8H67                               | NCT6776F   | N            | N            | P            | N            |
| ASUS     | P8Z68-V LX                          | NCT6776F   | N            | N            | P            | N            |
| ASUS     | PRIME A320I-K                       | IT8655E    | N            | N            | M            | N            |
| ASUS     | PRIME A320M-A                       | IT8655E    | N            | N            | M            | N            |
| ASUS     | PRIME A320M-C R2.0                  | IT8665E    | N            | N            | M            | N            |
| ASUS     | PRIME A320M-E                       | IT8655E    | N            | N            | M            | N            |
| ASUS     | PRIME A320M-F                       | IT8655E    | N            | N            | M            | N            |
| ASUS     | PRIME A320M-K                       | IT8655E    | N            | N            | M            | N            |
| ASUS     | PRIME A320M-K/BR                    | IT8655E    | N            | N            | M            | N            |
| ASUS     | PRIME A320M-R                       | IT8655E    | N            | N            | M            | N            |
| ASUS     | PRIME A520M-A                       | NCT6798D-R | N            | N            | Y            | N            |
| ASUS     | PRIME A520M-A II                    | NCT6798D-R | N            | N            | Y            | N            |
| ASUS     | PRIME A520M-E                       | NCT6798D-R | N            | N            | Y            | N            |
| ASUS     | PRIME A520M-K                       | NCT6798D-R | N            | N            | Y            | N            |
| ASUS     | PRIME A620M-A                       | NCT6799D-R | N            | N            | Y            | N            |
| ASUS     | PRIME B250-PLUS                     | NCT5539D   | F            | N            | F            | N            |
| ASUS     | PRIME B250M-A                       | NCT6793D   | F            | N            | F            | N            |
| ASUS     | PRIME B250M-C                       | NCT6793D   | N            | N            | P            | N            |
| ASUS     | PRIME B250M-J                       | NCT5539D   | N            | N            | P            | N            |
| ASUS     | PRIME B250M-K                       | NCT5539D   | F            | N            | F            | N            |
| ASUS     | PRIME B250M-PLUS                    | NCT5539D   | F            | N            | F            | N            |
| ASUS     | PRIME B350-PLUS                     | IT8655E    | N            | N            | M            | N            |
| ASUS     | PRIME B350M-A                       | IT8655E    | N            | N            | M            | N            |
| ASUS     | PRIME B350M-E                       | IT8655E    | N            | N            | M            | N            |
| ASUS     | PRIME B350M-K                       | IT8655E    | N            | N            | M            | N            |
| ASUS     | PRIME B360-PLUS                     | NCT5582D   | N            | N            | Y            | N            |
| ASUS     | PRIME B360M-A                       | NCT6796D   | N            | N            | Y            | N            |
| ASUS     | PRIME B360M-C                       | NCT6793D   | N            | N            | Y            | N            |
| ASUS     | PRIME B360M-D                       | NCT5582D   | N            | N            | Y            | N            |
| ASUS     | PRIME B360M-K                       | NCT5582D   | N            | N            | Y            | N            |
| ASUS     | PRIME B365-PLUS                     | NCT5582D   | N            | N            | P            | N            |
| ASUS     | PRIME B365M-A                       | NCT6796D   | N            | N            | P            | N            |
| ASUS     | PRIME B365M-C                       | NCT5582D   | N            | N            | P            | N            |
| ASUS     | PRIME B365M-K                       | NCT5582D   | N            | N            | P            | N            |
| ASUS     | PRIME B450-PLUS                     | IT8665E    | N            | N            | M            | N            |
| ASUS     | PRIME B450M-A                       | IT8655E    | N            | N            | M            | N            |
| ASUS     | PRIME B450M-A II                    | IT8655E    | N            | N            | M            | N            |
| ASUS     | PRIME B450M-GAMING II               | IT8655E    | N            | N            | M            | N            |
| ASUS     | PRIME B450M-GAMING/BR               | IT8655E    | N            | N            | M            | N            |
| ASUS     | PRIME B450M-K                       | IT8655E    | N            | N            | M            | N            |
| ASUS     | PRIME B450M-K II                    | IT8655E    | N            | N            | M            | N            |
| ASUS     | PRIME B460-PLUS                     | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME B460I-PLUS                    | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME B460M-A                       | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME B460M-A R2.0                  | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME B460M-K                       | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME B550-PLUS                     | NCT6798D-R | N            | N            | Y            | N            |
| ASUS     | PRIME B550-PLUS AC-HES              | NCT6798D-R | N            | N            | Y            | N            |
| ASUS     | PRIME B550M-A                       | NCT6798D-R | N            | N            | Y            | N            |
| ASUS     | PRIME B550M-A (WI-FI)               | NCT6798D-R | N            | N            | Y            | N            |
| ASUS     | PRIME B550M-A AC                    | NCT6798D-R | N            | N            | Y            | N            |
| ASUS     | PRIME B550M-A WIFI II               | NCT6798D-R | N            | N            | Y            | N            |
| ASUS     | PRIME B550M-K                       | NCT6798D-R | N            | N            | Y            | N            |
| ASUS     | PRIME B560-PLUS                     | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME B560-PLUS AC-HES              | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME B560M-A                       | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME B560M-A AC                    | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME B560M-K                       | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME B650-PLUS                     | NCT6799D-R | N            | N            | Y            | N            |
| ASUS     | PRIME B650M-A                       | NCT6799D-R | N            | N            | Y            | N            |
| ASUS     | PRIME B650M-A AX                    | NCT6799D-R | N            | N            | Y            | N            |
| ASUS     | PRIME B650M-A AX II                 | NCT6799D-R | N            | N            | Y            | N            |
| ASUS     | PRIME B650M-A II                    | NCT6799D-R | N            | N            | Y            | N            |
| ASUS     | PRIME B650M-A WIFI                  | NCT6799D-R | N            | N            | Y            | N            |
| ASUS     | PRIME B650M-A WIFI II               | NCT6799D-R | N            | N            | Y            | N            |
| ASUS     | PRIME B660-PLUS D4                  | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME B660M-A AC D4                 | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME B660M-A D4                    | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME B660M-A WIFI D4               | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME B660M-K D4                    | NCT6798D   | N            | N            | U            | N            |
| ASUS     | PRIME B760-PLUS                     | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME B760-PLUS D4                  | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME B760M-A                       | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME B760M-A AX D4                 | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME B760M-A D4                    | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME B760M-A WIFI                  | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME B760M-A WIFI D4               | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME B760M-AJ D4                   | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME B760M-K D4                    | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME H110M-P                       | NCT5539D   | L            | N            | L            | N            |
| ASUS     | PRIME H110M2                        | NCT6793D   | L            | N            | L            | N            |
| ASUS     | PRIME H270-PLUS                     | NCT5539D   | N            | N            | P            | N            |
| ASUS     | PRIME H270-PRO                      | NCT5539D   | F            | N            | F            | N            |
| ASUS     | PRIME H270M-PLUS                    | NCT5539D   | F            | N            | F            | N            |
| ASUS     | PRIME H310-PLUS                     | NCT5582D   | N            | N            | Y            | N            |
| ASUS     | PRIME H310-PLUS R2.0                | NCT6796D   | N            | N            | P            | N            |
| ASUS     | PRIME H310I-PLUS                    | NCT6793D   | N            | N            | Y            | N            |
| ASUS     | PRIME H310I-PLUS R2.0               | NCT5582D   | N            | N            | P            | N            |
| ASUS     | PRIME H310M-A                       | NCT5582D   | N            | N            | Y            | N            |
| ASUS     | PRIME H310M-A R2.0                  | NCT5582D   | N            | N            | P            | N            |
| ASUS     | PRIME H310M-C                       | NCT6793D   | N            | N            | Y            | N            |
| ASUS     | PRIME H310M-C R2.0                  | NCT6793D   | N            | N            | P            | N            |
| ASUS     | PRIME H310M-C/PS R2.0               | NCT6793D   | N            | N            | P            | N            |
| ASUS     | PRIME H310M-CS R2.0                 | NCT6798D   | N            | N            | P            | N            |
| ASUS     | PRIME H310M-D                       | NCT6796D   | N            | N            | Y            | N            |
| ASUS     | PRIME H310M-D R2.0                  | NCT6796D   | N            | N            | P            | N            |
| ASUS     | PRIME H310M-DASH                    | NCT6793D   | N            | N            | Y            | N            |
| ASUS     | PRIME H310M-DASH R2.0               | NCT6793D   | N            | N            | P            | N            |
| ASUS     | PRIME H310M-E                       | NCT5582D   | N            | N            | Y            | N            |
| ASUS     | PRIME H310M-E R2.0                  | NCT5582D   | N            | N            | P            | N            |
| ASUS     | PRIME H310M-E R2.0/BR               | NCT5582D   | N            | N            | P            | N            |
| ASUS     | PRIME H310M-E/BR                    | NCT5582D   | N            | N            | Y            | N            |
| ASUS     | PRIME H310M-F                       | NCT6793D   | N            | N            | Y            | N            |
| ASUS     | PRIME H310M-F R2.0                  | NCT6798D   | N            | N            | P            | N            |
| ASUS     | PRIME H310M-K                       | NCT5582D   | N            | N            | Y            | N            |
| ASUS     | PRIME H310M-K R2.0                  | NCT5582D   | N            | N            | P            | N            |
| ASUS     | PRIME H310M-R R2.0                  | NCT6798D   | N            | N            | P            | N            |
| ASUS     | PRIME H310M2 R2.0                   | NCT6793D   | F            | N            | F            | N            |
| ASUS     | PRIME H310T                         | NCT5582D   | N            | N            | Y            | N            |
| ASUS     | PRIME H310T R2.0                    | NCT5582D   | F            | N            | F            | N            |
| ASUS     | PRIME H370-A                        | NCT5582D   | N            | N            | Y            | N            |
| ASUS     | PRIME H370-PLUS                     | NCT5582D   | N            | N            | Y            | N            |
| ASUS     | PRIME H370M-PLUS                    | NCT5582D   | N            | N            | Y            | N            |
| ASUS     | PRIME H410I-PLUS                    | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME H410M-A                       | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME H410M-D                       | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME H410M-E                       | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME H410M-F                       | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME H410M-K                       | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME H410M-K R2.0                  | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME H410M-R                       | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME H470-PLUS                     | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME H470M-PLUS                    | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME H510M-A                       | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME H510M-A WIFI                  | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME H510M-D                       | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME H510M-E                       | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME H510M-F                       | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME H510M-K                       | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME H510M-K R2.0                  | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME H510M-R                       | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME H510T2/CSM                    | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME H570-PLUS                     | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME H570M-PLUS                    | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME H610I-PLUS D4                 | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME H610M-A D4                    | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME H610M-A WIFI D4               | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME H610M-D D4                    | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME H610M-E D4                    | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME H610M-F D4                    | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME H610M-K D4                    | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME H610M-R D4                    | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME H670-PLUS D4                  | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME H770-PLUS D4                  | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME Q270M-C                       | NCT6793D   | F            | N            | F            | N            |
| ASUS     | PRIME Q370M-C                       | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME TRX40-PRO                     | NCT6798D   | L            | N            | L            | N            |
| ASUS     | PRIME TRX40-PRO S                   | NCT6798D   | L            | N            | L            | N            |
| ASUS     | PRIME X299 EDITION 30               | NCT6798D   | L            | N            | L            | N            |
| ASUS     | PRIME X299-A                        | NCT6796D   | L            | N            | L            | N            |
| ASUS     | PRIME X299-A II                     | NCT6798D   | L            | N            | L            | N            |
| ASUS     | PRIME X299-DELUXE                   | NCT6796D   | L            | N            | L            | N            |
| ASUS     | PRIME X299-DELUXE II                | NCT6796D   | L            | N            | L            | N            |
| ASUS     | PRIME X370-A                        | IT8655E    | L            | N            | L            | N            |
| ASUS     | PRIME X370-PRO                      | IT8665E    | N            | N            | M            | N            |
| ASUS     | PRIME X399-A                        |            | Y            | N            | P            | N            |
| ASUS     | PRIME X470-PRO                      | IT8665E    | Y            | N            | M            | Y            |
| ASUS     | PRIME X570-P                        | NCT6798D-R | N            | N            | Y            | N            |
| ASUS     | PRIME X570-PRO                      | NCT6798D-R | N            | N            | Y            | Y            |
| ASUS     | PRIME X670-P                        | NCT6799D-R | N            | N            | Y            | N            |
| ASUS     | PRIME X670-P WIFI                   | NCT6799D-R | N            | N            | Y            | N            |
| ASUS     | PRIME X670E-PRO WIFI                | NCT6799D-R | N            | N            | Y            | N            |
| ASUS     | PRIME Z270-A                        | NCT6793D   | N            | N            | P            | N            |
| ASUS     | PRIME Z270-K                        | NCT5539D   | F            | N            | F            | N            |
| ASUS     | PRIME Z270-P                        | NCT5539D   | F            | N            | F            | N            |
| ASUS     | PRIME Z270M-PLUS                    | NCT5539D   | F            | N            | F            | N            |
| ASUS     | PRIME Z370-A                        | NCT6793D   | F            | N            | F            | N            |
| ASUS     | PRIME Z370-A II                     | NCT6793D   | F            | N            | F            | N            |
| ASUS     | PRIME Z370-P                        | NCT6793D   | L            | N            | L            | N            |
| ASUS     | PRIME Z370-P II                     | NCT6793D   | L            | N            | L            | N            |
| ASUS     | PRIME Z370M-PLUS II                 | NCT6793D   | L            | N            | L            | N            |
| ASUS     | PRIME Z390-A                        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME Z390-A/H10                    | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME Z390-P                        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME Z390M-PLUS                    | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME Z490-A                        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME Z490-P                        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME Z490-V                        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME Z490M-PLUS                    | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME Z590-A                        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME Z590-P                        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME Z590-P WIFI                   | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME Z590-V                        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME Z590M-PLUS                    | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME Z690-A                        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME Z690-P                        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME Z690-P D4                     | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME Z690-P WIFI                   | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME Z690-P WIFI D4                | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME Z690M-HZ                      | NCT6798D   | L            | N            | L            | N            |
| ASUS     | PRIME Z690M-PLUS D4                 | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME Z790-A WIFI                   | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME Z790-P                        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME Z790-P D4                     | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME Z790-P WIFI                   | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME Z790-P WIFI D4                | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME Z790M-PLUS                    | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRIME Z790M-PLUS D4                 | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRO A320M-R WI-FI                   | IT8655E    | N            | N            | M            | N            |
| ASUS     | PRO B460M-C                         | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRO H310M-R R2.0 WI-FI              | NCT6793D   | N            | N            | P            | N            |
| ASUS     | PRO H410M-C                         | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRO H410T                           | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | PRO Q470M-C                         | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | Pro A520M-C                         | NCT6798D-R | N            | N            | Y            | N            |
| ASUS     | Pro A520M-C II                      | NCT6798D-R | N            | N            | Y            | N            |
| ASUS     | Pro B550M-C                         | NCT6798D-R | N            | N            | Y            | N            |
| ASUS     | Pro B560M-C                         | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | Pro B560M-CT                        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | Pro B660M-C                         | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | Pro B660M-C D4                      | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | Pro B760M-C                         | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | Pro B760M-CT                        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | Pro H510M-C                         | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | Pro H510M-CT                        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | Pro H610M-C                         | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | Pro H610M-C D4                      | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | Pro H610M-CT D4                     | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | Pro H610T D4                        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | Pro Q670M-C                         | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | Pro WS C246-ACE                     |            | L            | N            | L            | N            |
| ASUS     | Pro WS C422-ACE                     |            | N            | N            | P            | N            |
| ASUS     | Pro WS W480-ACE                     |            | L            | N            | L            | N            |
| ASUS     | Pro WS W680-ACE                     | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | Pro WS W680-ACE IPMI                | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | Pro WS W790-ACE                     | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | Pro WS W790E-SAGE SE                | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | Pro WS WRX80E-SAGE SE WIFI          | NCT6798D-R | N            | N            | P            | N            |
| ASUS     | Pro WS WRX80E-SAGE SE WIFI II       | NCT6798D-R | N            | N            | P            | N            |
| ASUS     | Pro WS X299 SAGE II                 | NCT6798D   | L            | N            | L            | N            |
| ASUS     | Pro WS X570-ACE                     | NCT6798D-R | N            | N            | Y            | Y            |
| ASUS     | ProArt B550-CREATOR                 | NCT6798D-R | N            | N            | Y            | Y            |
| ASUS     | ProArt B650-CREATOR                 | NCT6799D-R | N            | N            | Y            | N            |
| ASUS     | ProArt B660-CREATOR D4              | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ProArt B760-CREATOR                 | NCT6798D   | L            | N            | L            | N            |
| ASUS     | ProArt B760-CREATOR D4              | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ProArt X570-CREATOR WIFI            | NCT6798D-R | N            | N            | Y            | Y            |
| ASUS     | ProArt X670E-CREATOR WIFI           | NCT6799D-R | N            | N            | Y            | N            |
| ASUS     | ProArt Z490-CREATOR 10G             | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ProArt Z690-CREATOR WIFI            | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ProArt Z790-CREATOR WIFI            | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | Q370I-IM-A R2.0                     | NCT6116D   | N            | N            | N            | N            |
| GIGABYTE | Q87M-D2H                            |            | N            | N            | N            | N            |
| ASUS     | RAMPAGE III BLACK EDITION           |            | L            | N            | L            | N            |
| ASUS     | RAMPAGE IV BLACK EDITION            |            | L            | N            | L            | N            |
| ASUS     | RAMPAGE IV EXTREME                  |            | L            | N            | L            | N            |
| ASUS     | RAMPAGE IV FORMULA                  |            | L            | N            | L            | N            |
| ASUS     | RAMPAGE IV GENE                     |            | L            | N            | L            | N            |
| ASUS     | RAMPAGE V EDITION 10                |            | F            | N            | F            | N            |
| ASUS     | RAMPAGE V EXTREME                   |            | N            | N            | P            | N            |
| ASUS     | ROG CROSSHAIR VI EXTREME            | IT8655E    | Y            | N            | M            | U            |
| ASUS     | ROG CROSSHAIR VI HERO (WI-FI AC)    | IT8655E    | Y            | N            | M            | U            |
| ASUS     | ROG CROSSHAIR VII HERO              | IT8665E    | Y            | N            | M            | U            |
| ASUS     | ROG CROSSHAIR VII HERO (WI-FI)      | IT8665E    | Y            | N            | M            | U            |
| ASUS     | ROG CROSSHAIR VIII DARK HERO        | NCT6798D-R | N            | N            | Y            | Y            |
| ASUS     | ROG CROSSHAIR VIII EXTREME          | NCT6798D-R | N            | N            | Y            | U            |
| ASUS     | ROG CROSSHAIR VIII FORMULA          | NCT6798D-R | N            | N            | Y            | Y            |
| ASUS     | ROG CROSSHAIR VIII HERO             | NCT6798D-R | N            | N            | Y            | Y            |
| ASUS     | ROG CROSSHAIR VIII HERO (WI-FI)     | NCT6798D-R | N            | N            | Y            | Y            |
| ASUS     | ROG CROSSHAIR VIII IMPACT           | NCT6798D-R | N            | N            | Y            | Y            |
| ASUS     | ROG CROSSHAIR X670E EXTREME         | NCT6799D-R | N            | N            | Y            | N            |
| ASUS     | ROG CROSSHAIR X670E GENE            | NCT6799D-R | N            | N            | Y            | N            |
| ASUS     | ROG CROSSHAIR X670E HERO            | NCT6799D-R | N            | N            | Y            | N            |
| ASUS     | ROG DOMINUS EXTREME                 |            | N            | N            | P            | N            |
| ASUS     | ROG MAXIMUS X APEX                  | NCT6793D   | L            | N            | L            | N            |
| ASUS     | ROG MAXIMUS X CODE                  | NCT6793D   | L            | N            | L            | N            |
| ASUS     | ROG MAXIMUS X FORMULA               | NCT6793D   | L            | N            | L            | N            |
| ASUS     | ROG MAXIMUS X HERO                  | NCT6793D   | N            | N            | P            | N            |
| ASUS     | ROG MAXIMUS X HERO (WI-FI AC)       | NCT6793D   | L            | N            | L            | N            |
| ASUS     | ROG MAXIMUS XI APEX                 | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG MAXIMUS XI CODE                 | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG MAXIMUS XI EXTREME              | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG MAXIMUS XI FORMULA              | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG MAXIMUS XI GENE                 | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG MAXIMUS XI HERO                 | NCT6798D   | N            | N            | Y            | N?           |
| ASUS     | ROG MAXIMUS XI HERO (WI-FI)         | NCT6798D   | N            | N            | Y            | N?           |
| ASUS     | ROG MAXIMUS XII APEX                | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG MAXIMUS XII EXTREME             | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG MAXIMUS XII FORMULA             | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG MAXIMUS XII HERO (WI-FI)        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG MAXIMUS XIII APEX               | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG MAXIMUS XIII EXTREME            | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG MAXIMUS XIII EXTREME GLACIAL    | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG MAXIMUS XIII HERO               | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG MAXIMUS Z690 APEX               | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG MAXIMUS Z690 EXTREME            | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG MAXIMUS Z690 EXTREME GLACIAL    | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG MAXIMUS Z690 FORMULA            | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG MAXIMUS Z690 HERO               | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG MAXIMUS Z690 HERO EVA           | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG MAXIMUS Z790 APEX               | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG MAXIMUS Z790 EXTREME            | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG MAXIMUS Z790 HERO               | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG RAMPAGE VI APEX                 | NCT6798D   | L            | N            | L            | N            |
| ASUS     | ROG RAMPAGE VI EXTREME ENCORE       | NCT6798D   | N            | N            | P            | N            |
| ASUS     | ROG RAMPAGE VI EXTREME OMEGA        | NCT6798D   | L            | N            | L            | N            |
| ASUS     | ROG STRIX B350-F GAMING             | IT8665E    | N            | N            | M            | N            |
| ASUS     | ROG STRIX B350-I GAMING             | IT8665E    | N            | N            | M            | N            |
| ASUS     | ROG STRIX B360-F GAMING             | NCT6796D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX B360-G GAMING             | NCT5582D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX B360-H GAMING             | NCT5582D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX B360-H GAMING/OPTANE      | NCT5582D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX B360-I GAMING             | NCT6796D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX B365-F GAMING             | NCT6796D   | N            | N            | P            | N            |
| ASUS     | ROG STRIX B365-G GAMING             | NCT6796D   | N            | N            | P            | N            |
| ASUS     | ROG STRIX B450-E GAMING             | IT8655E    | Y            | N            | M            | U            |
| ASUS     | ROG STRIX B450-F GAMING             | IT8665E    | Y            | N            | M            | U            |
| ASUS     | ROG STRIX B450-F GAMING II          | IT8665E    | Y            | N            | M            | U            |
| ASUS     | ROG STRIX B450-I GAMING             | IT8655E    | Y            | N            | M            | U            |
| ASUS     | ROG STRIX B460-F GAMING             | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX B460-G GAMING             | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX B460-H GAMING             | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX B460-I GAMING             | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX B550-A GAMING             | NCT6798D-R | N            | N            | Y            | N            |
| ASUS     | ROG STRIX B550-E GAMING             | NCT6798D-R | N            | N            | Y            | Y            |
| ASUS     | ROG STRIX B550-F GAMING             | NCT6798D-R | N            | N            | Y            | N            |
| ASUS     | ROG STRIX B550-F GAMING (WI-FI)     | NCT6798D-R | N            | N            | Y            | N            |
| ASUS     | ROG STRIX B550-F GAMING WIFI II     | NCT6798D-R | N            | N            | Y            | N            |
| ASUS     | ROG STRIX B550-I GAMING             | NCT6798D-R | N            | N            | Y            | Y            |
| ASUS     | ROG STRIX B550-XE GAMING WIFI       | NCT6798D-R | N            | N            | Y            | U            |
| ASUS     | ROG STRIX B560-A GAMING WIFI        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX B560-E GAMING WIFI        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX B560-F GAMING WIFI        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX B560-G GAMING WIFI        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX B560-I GAMING WIFI        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX B650-A GAMING WIFI        | NCT6799D-R | N            | N            | Y            | N            |
| ASUS     | ROG STRIX B650E-E GAMING WIFI       | NCT6799D-R | N            | N            | Y            | N            |
| ASUS     | ROG STRIX B650E-F GAMING WIFI       | NCT6799D-R | N            | N            | Y            | N            |
| ASUS     | ROG STRIX B650E-I GAMING WIFI       | NCT6799D-R | N            | N            | Y            | N            |
| ASUS     | ROG STRIX B660-A GAMING WIFI        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX B660-A GAMING WIFI D4     | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX B660-F GAMING WIFI        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX B660-G GAMING WIFI        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX B660-I GAMING WIFI        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX B760-A GAMING WIFI        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX B760-A GAMING WIFI D4     | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX B760-F GAMING WIFI        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX B760-G GAMING WIFI        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX B760-G GAMING WIFI D4     | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX B760-I GAMING WIFI        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX H370-F GAMING             | NCT6796D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX H370-I GAMING             | NCT6796D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX H470-I GAMING             | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX TRX40-E GAMING            | NCT6798D   | N            | N            | P            | N            |
| ASUS     | ROG STRIX TRX40-XE GAMING           | NCT6798D   | N            | N            | P            | N            |
| ASUS     | ROG STRIX X299-E GAMING             | NCT6796D   | L            | N            | L            | N            |
| ASUS     | ROG STRIX X299-E GAMING II          | NCT6798D   | L            | N            | L            | N            |
| ASUS     | ROG STRIX X299-XE GAMING            | NCT6798D   | L            | N            | L            | N            |
| ASUS     | ROG STRIX X370-F GAMING             | IT8665E    | N            | N            | M            | N            |
| ASUS     | ROG STRIX X370-I GAMING             | IT8665E    | N            | N            | M            | N            |
| ASUS     | ROG STRIX X399-E GAMING             |            | F            | N            | F            | N            |
| ASUS     | ROG STRIX X470-F GAMING             | IT8665E    | Y            | N            | M            | U            |
| ASUS     | ROG STRIX X470-I GAMING             | IT8665E    | Y            | N            | M            | U            |
| ASUS     | ROG STRIX X570-E GAMING             | NCT6798D-R | N            | N            | Y            | Y            |
| ASUS     | ROG STRIX X570-E GAMING WIFI II     | NCT6798D-R | N            | N            | Y            | Y            |
| ASUS     | ROG STRIX X570-F GAMING             | NCT6798D-R | N            | N            | Y            | Y            |
| ASUS     | ROG STRIX X570-I GAMING             | NCT6798D-R | N            | N            | Y            | Y            |
| ASUS     | ROG STRIX X670E-A GAMING WIFI       | NCT6799D-R | N            | N            | Y            | N            |
| ASUS     | ROG STRIX X670E-E GAMING WIFI       | NCT6799D-R | N            | N            | Y            | N            |
| ASUS     | ROG STRIX X670E-F GAMING WIFI       | NCT6799D-R | N            | N            | Y            | N            |
| ASUS     | ROG STRIX X670E-I GAMING WIFI       | NCT6799D-R | N            | N            | Y            | N            |
| ASUS     | ROG STRIX Z270-I GAMING             | NCT6793D   | L            | N            | L            | N            |
| ASUS     | ROG STRIX Z270E GAMING              | NCT6793D   | L            | N            | L            | N            |
| ASUS     | ROG STRIX Z270F GAMING              | NCT6793D   | L            | N            | L            | N            |
| ASUS     | ROG STRIX Z270G GAMING              | NCT6793D   | L            | N            | L            | N            |
| ASUS     | ROG STRIX Z270H GAMING              | NCT6793D   | L            | N            | L            | N            |
| ASUS     | ROG STRIX Z370-E GAMING             | NCT6793D   | F            | N            | F            | N            |
| ASUS     | ROG STRIX Z370-F GAMING             | NCT6793D   | L            | N            | L            | N            |
| ASUS     | ROG STRIX Z370-G GAMING             | NCT6793D   | F            | N            | F            | N            |
| ASUS     | ROG STRIX Z370-G GAMING (WI-FI AC)  | NCT6793D   | L            | N            | L            | N            |
| ASUS     | ROG STRIX Z370-H GAMING             | NCT6793D   | N            | N            | P            | N            |
| ASUS     | ROG STRIX Z370-I GAMING             | NCT6793D   | L            | N            | L            | N            |
| ASUS     | ROG STRIX Z390-E GAMING             | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX Z390-F GAMING             | NCT6798D   | N            | N            | Y            | N?           |
| ASUS     | ROG STRIX Z390-H GAMING             | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX Z390-I GAMING             | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX Z490-A GAMING             | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX Z490-E GAMING             | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX Z490-F GAMING             | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX Z490-G GAMING             | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX Z490-G GAMING (WI-FI)     | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX Z490-H GAMING             | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX Z490-I GAMING             | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX Z590-A GAMING WIFI        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX Z590-A GAMING WIFI II     | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX Z590-E GAMING WIFI        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX Z590-F GAMING WIFI        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX Z590-I GAMING WIFI        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX Z690-A GAMING WIFI        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX Z690-A GAMING WIFI D4     | NCT6798D   | N            | N            | Y            | N?           |
| ASUS     | ROG STRIX Z690-E GAMING WIFI        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX Z690-F GAMING WIFI        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX Z690-G GAMING WIFI        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX Z690-I GAMING WIFI        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX Z790-A GAMING WIFI        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX Z790-A GAMING WIFI D4     | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX Z790-E GAMING WIFI        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX Z790-F GAMING WIFI        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX Z790-H GAMING WIFI        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG STRIX Z790-I GAMING WIFI        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | ROG ZENITH EXTREME                  |            | F            | N            | F            | N            |
| ASUS     | ROG ZENITH EXTREME ALPHA            |            | F            | N            | F            | N            |
| ASUS     | ROG ZENITH II EXTREME               | NCT6798D   | N            | N            | P            | N?           |
| ASUS     | ROG ZENITH II EXTREME ALPHA         | NCT6798D   | N            | N            | P            | N?           |
| LENOVO   | S206                                |            | N            | N            | N            | N            |
| ASUS     | STRIX B250F GAMING                  | NCT6793D   | F            | N            | F            | N            |
| ASUS     | STRIX B250G GAMING                  | NCT5539D   | F            | N            | F            | N            |
| ASUS     | STRIX B250H GAMING                  | NCT5539D   | F            | N            | F            | N            |
| ASUS     | STRIX B250I GAMING                  | NCT6793D   | F            | N            | F            | N            |
| ASUS     | STRIX H270F GAMING                  | NCT6793D   | F            | N            | F            | N            |
| ASUS     | STRIX H270I GAMING                  | NCT5539D   | F            | N            | F            | N            |
| ASUS     | STRIX X99 GAMING                    |            | L            | N            | L            | N            |
| ASUS     | STRIX Z270E GAMING                  | NCT6793D   | N            | N            | P            | N            |
| ASUS     | STRIX Z270F GAMING                  | NCT6793D   | N            | N            | P            | N            |
| ASUS     | STRIX Z270G GAMING                  | NCT6793D   | N            | N            | P            | N            |
| ASUS     | STRIX Z270H GAMING                  | NCT6793D   | N            | N            | P            | N            |
| ASUS     | STRIX Z270I GAMING                  | NCT6793D   | F            | N            | F            | N            |
| ASUS     | TUF B350M-PLUS GAMING               | IT8655E    | N            | N            | M            | N            |
| ASUS     | TUF B360-PLUS GAMING                | NCT5582D   | N            | N            | Y            | N            |
| ASUS     | TUF B360-PRO GAMING                 | NCT5582D   | N            | N            | Y            | N            |
| ASUS     | TUF B360-PRO GAMING (WI-FI)         | NCT5582D   | N            | N            | Y            | N            |
| ASUS     | TUF B360-PRO GAMING WIFI            |            | L            | N            | L            | N            |
| ASUS     | TUF B360M-E GAMING                  | NCT5582D   | N            | N            | Y            | N            |
| ASUS     | TUF B360M-PLUS GAMING               | NCT5582D   | N            | N            | Y            | N            |
| ASUS     | TUF B360M-PLUS GAMING S             | NCT5582D   | N            | N            | Y            | N            |
| ASUS     | TUF B360M-PLUS GAMING/BR            | NCT5582D   | N            | N            | Y            | N            |
| ASUS     | TUF B365-PLUS GAMING                | NCT5582D   | N            | N            | P            | N            |
| ASUS     | TUF B365M-PLUS GAMING               | NCT5582D   | N            | N            | P            | N            |
| ASUS     | TUF B450-PLUS GAMING                | IT8665E    | N            | N            | M            | N            |
| ASUS     | TUF B450-PRO GAMING                 | IT8665E    | N            | N            | M            | N            |
| ASUS     | TUF B450M-PLUS GAMING               | IT8655E    | N            | N            | M            | N            |
| ASUS     | TUF B450M-PRO GAMING                | IT8655E    | N            | N            | M            | N            |
| ASUS     | TUF GAMING A520M-PLUS               | NCT6798D-R | N            | N            | Y            | N            |
| ASUS     | TUF GAMING A520M-PLUS II            | NCT6798D-R | N            | N            | Y            | N            |
| ASUS     | TUF GAMING A520M-PLUS WIFI          | NCT6798D-R | N            | N            | Y            | N            |
| ASUS     | TUF GAMING A620M-PLUS               | NCT6799D-R | N            | N            | Y            | N            |
| ASUS     | TUF GAMING A620M-PLUS WIFI          | NCT6799D-R | N            | N            | Y            | N            |
| ASUS     | TUF GAMING B450-PLUS II             | IT8665E    | N            | N            | M            | N            |
| ASUS     | TUF GAMING B450M-PLUS II            | IT8655E    | N            | N            | M            | N            |
| ASUS     | TUF GAMING B450M-PRO II             | IT8655E    | N            | N            | M            | N            |
| ASUS     | TUF GAMING B450M-PRO S              | IT8655E    | N            | N            | M            | N            |
| ASUS     | TUF GAMING B460-PLUS                | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF GAMING B460-PRO (WI-FI)         | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF GAMING B460M-PLUS               | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF GAMING B460M-PLUS (WI-FI)       | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF GAMING B460M-PRO                | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF GAMING B550-PLUS                | NCT6798D-R | N            | N            | Y            | N            |
| ASUS     | TUF GAMING B550-PLUS (WI-FI)        | NCT6798D-R | N            | N            | Y            | N            |
| ASUS     | TUF GAMING B550-PLUS WIFI II        | NCT6798D-R | N            | N            | Y            | N            |
| ASUS     | TUF GAMING B550-PRO                 | NCT6798D-R | N            | N            | Y            | N            |
| ASUS     | TUF GAMING B550M ZAKU (WI-FI)       | NCT6798D-R | N            | N            | Y            | N            |
| ASUS     | TUF GAMING B550M-E                  | NCT6798D-R | N            | N            | Y            | N            |
| ASUS     | TUF GAMING B550M-E WIFI             | NCT6798D-R | N            | N            | Y            | N            |
| ASUS     | TUF GAMING B550M-PLUS               | NCT6798D-R | N            | N            | Y            | N            |
| ASUS     | TUF GAMING B550M-PLUS (WI-FI)       | NCT6798D-R | N            | N            | Y            | N            |
| ASUS     | TUF GAMING B550M-PLUS WIFI II       | NCT6798D-R | N            | N            | Y            | N            |
| ASUS     | TUF GAMING B560-PLUS WIFI           | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF GAMING B560M-E                  | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF GAMING B560M-PLUS               | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF GAMING B560M-PLUS WIFI          | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF GAMING B650-PLUS                | NCT6799D-R | N            | N            | Y            | N            |
| ASUS     | TUF GAMING B650-PLUS WIFI           | NCT6799D-R | N            | N            | Y            | N            |
| ASUS     | TUF GAMING B650M-PLUS               | NCT6799D-R | N            | N            | Y            | N            |
| ASUS     | TUF GAMING B650M-PLUS WIFI          | NCT6799D-R | N            | N            | Y            | N            |
| ASUS     | TUF GAMING B660-PLUS WIFI D4        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF GAMING B660M-E D4               | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF GAMING B660M-PLUS D4            | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF GAMING B660M-PLUS WIFI          | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF GAMING B660M-PLUS WIFI D4       | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF GAMING B760-PLUS WIFI           | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF GAMING B760-PLUS WIFI D4        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF GAMING B760M-BTF WIFI D4        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF GAMING B760M-E D4               | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF GAMING B760M-PLUS               | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF GAMING B760M-PLUS D4            | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF GAMING B760M-PLUS WIFI          | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF GAMING B760M-PLUS WIFI D4       | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF GAMING H470-PRO                 | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF GAMING H470-PRO (WI-FI)         | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF GAMING H570-PRO                 | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF GAMING H570-PRO WIFI            | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF GAMING H670-PRO WIFI D4         | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF GAMING H770-PRO WIFI            | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF GAMING X570-PLUS                | NCT6798D-R | N            | N            | Y            | N            |
| ASUS     | TUF GAMING X570-PLUS (WI-FI)        | NCT6798D-R | N            | N            | Y            | N            |
| ASUS     | TUF GAMING X570-PLUS_BR             | NCT6798D-R | N            | N            | Y            | N            |
| ASUS     | TUF GAMING X570-PRO (WI-FI)         | NCT6798D-R | N            | N            | Y            | N            |
| ASUS     | TUF GAMING X570-PRO WIFI II         | NCT6798D-R | N            | N            | Y            | N            |
| ASUS     | TUF GAMING X670E-PLUS               | NCT6799D-R | N            | N            | Y            | N            |
| ASUS     | TUF GAMING X670E-PLUS WIFI          | NCT6799D-R | N            | N            | Y            | N            |
| ASUS     | TUF GAMING Z490-PLUS                | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF GAMING Z490-PLUS (WI-FI)        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF GAMING Z590-PLUS                | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF GAMING Z590-PLUS WIFI           | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF GAMING Z690-PLUS                | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF GAMING Z690-PLUS D4             | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF GAMING Z690-PLUS WIFI           | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF GAMING Z690-PLUS WIFI D4        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF GAMING Z790-PLUS D4             | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF GAMING Z790-PLUS WIFI           | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF GAMING Z790-PLUS WIFI D4        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF H310-PLUS GAMING                | NCT6793D   | N            | N            | Y            | N            |
| ASUS     | TUF H310M-PLUS GAMING               | NCT5582D   | N            | N            | Y            | N            |
| ASUS     | TUF H310M-PLUS GAMING R2.0          | NCT6793D   | N            | N            | P            | N            |
| ASUS     | TUF H310M-PLUS GAMING/BR            | NCT5582D   | N            | N            | Y            | N            |
| ASUS     | TUF H370-PRO GAMING                 | NCT5582D   | N            | N            | Y            | N            |
| ASUS     | TUF H370-PRO GAMING (WI-FI)         | NCT5582D   | N            | N            | Y            | N            |
| ASUS     | TUF H370-PRO GAMING WIFI            |            | L            | N            | L            | N            |
| ASUS     | TUF X299 MARK 1                     | NCT6796D   | L            | N            | L            | N            |
| ASUS     | TUF X299 MARK 2                     | NCT6796D   | L            | N            | L            | N            |
| ASUS     | TUF X470-PLUS GAMING                | IT8665E    | N            | N            | M            | N            |
| ASUS     | TUF Z270 MARK 1                     | NCT6793D   | N            | N            | P            | N            |
| ASUS     | TUF Z370-PLUS GAMING                | NCT6793D   | L            | N            | L            | N            |
| ASUS     | TUF Z370-PLUS GAMING II             | NCT6793D   | L            | N            | L            | N            |
| ASUS     | TUF Z370-PRO GAMING                 | NCT6793D   | L            | N            | L            | N            |
| ASUS     | TUF Z390-PLUS GAMING                | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF Z390-PLUS GAMING (WI-FI)        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF Z390-PRO GAMING                 | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF Z390M-PRO GAMING                | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | TUF Z390M-PRO GAMING (WI-FI)        | NCT6798D   | N            | N            | Y            | N            |
| ASUS     | WS C246 PRO                         |            | L            | N            | L            | N            |
| ASUS     | WS C246M PRO                        |            | L            | N            | L            | N            |
| ASUS     | WS C422 DC                          |            | L            | N            | L            | N            |
| ASUS     | WS C422 PRO/SE                      |            | L            | N            | L            | N            |
| ASUS     | WS C422 SAGE/10G                    |            | L            | N            | L            | N            |
| ASUS     | WS C621E SAGE                       |            | L            | N            | L            | N            |
| ASUS     | WS X299 PRO                         | NCT6796D   | L            | N            | L            | N            |
| ASUS     | WS X299 PRO/SE                      | NCT6798D   | L            | N            | L            | N            |
| ASUS     | WS X299 SAGE                        | NCT6796D   | L            | N            | L            | N            |
| ASUS     | WS X299 SAGE/10G                    | NCT6796D   | L            | N            | L            | N            |
| ASUS     | WS Z390 PRO                         | NCT6798D   | N            | N            | Y            | N            |
| GIGABYTE | X299 UD4-CF                         |            | N            | U            | N            | N            |
| ASROCK   | X370 Gaming X                       |            | N            | N            | P            | N            |
| ASROCK   | X399 Taichi                         |            | N            | N            | P            | N            |
| GIGABYTE | X470 AORUS ULTRA GAMING-CF          |            | N            | U            | N            | N            |
| GIGABYTE | X570 AORUS ELITE                    |            | N            | Y            | N            | N            |
| GIGABYTE | X570 AORUS ELITE WIFI               | IT8688E    | N            | Y            | N            | N            |
| GIGABYTE | X570 AORUS MASTER                   | IT8688E    | N            | U            | N            | N            |
| GIGABYTE | X570 GAMING X                       |            | N            | Y            | N            | N            |
| GIGABYTE | X570 I AORUS PRO WIFI               | IT8688E    | N            | Y            | N            | N            |
| ASROCK   | X570 Steel Legend                   |            | N            | N            | P            | N            |
| ASROCK   | X570 Taichi                         |            | N            | N            | P            | N            |
| GIGABYTE | X570 UD                             |            | N            | Y            | N            | N            |
| ASUS     | X570DD                              |            | L            | N            | L            | N            |
| ASUS     | X570UD                              |            | L            | N            | L            | N            |
| ASUS     | X570ZD                              |            | L            | N            | L            | N            |
| GIGABYTE | X79-UP4                             |            | N            | N            | N            | N            |
| ASUS     | X99-E WS                            |            | N            | N            | P            | N            |
| ASUS     | X99-E WS/USB 3.1                    | NCT6791D   | N            | N            | P            | N            |
| ASUS     | X99-E-10G WS                        |            | F            | N            | F            | N            |
| GIGABYTE | X99-UD4-CF                          |            | N            | N            | N            | N            |
| ASROCK   | Z170 Extreme4                       |            | N            | N            | P            | N            |
| ASUS     | Z170 PRO GAMING                     | NCT6793D   | N            | N            | P            | N            |
| ASUS     | Z170 PRO GAMING/AURA                | NCT6793D   | N            | N            | P            | N            |
| ASUS     | Z170-A                              | NCT6793D   | N            | N            | P            | N            |
| ASUS     | Z170-DELUXE                         | NCT6793D   | N            | N            | P            | N            |
| ASUS     | Z170I PRO GAMING                    | NCT5539D   | N            | N            | P            | N            |
| ASUS     | Z170M-PLUS                          | NCT6793D   | N            | N            | P            | N            |
| ASUS     | Z270-WS                             | NCT6793D   | N            | N            | P            | N            |
| GIGABYTE | Z270N-WIFI-CF                       |            | N            | N            | N            | N            |
| GIGABYTE | Z390 I AORUS PRO WIFI-CF            |            | N            | Y            | N            | N            |
| GIGABYTE | Z490 AORUS ELITE AC                 | IT8688E    | N            | Y            | N            | N            |
| ASUS     | Z490-GUNDAM (WI-FI)                 | NCT6798D   | N            | N            | Y            | N            |
| GIGABYTE | Z590 AORUS ELITE AX                 |            | N            | U            | N            | N            |
| GIGABYTE | Z590 AORUS MASTER                   |            | N            | U            | N            | N            |
| GIGABYTE | Z590 AORUS PRO AX                   |            | N            | U            | N            | N            |
| GIGABYTE | Z590 AORUS ULTRA                    |            | N            | U            | N            | N            |
| GIGABYTE | Z590 D                              |            | N            | U            | N            | N            |
| GIGABYTE | Z590 GAMING X                       |            | N            | U            | N            | N            |
| GIGABYTE | Z590 UD                             |            | N            | U            | N            | N            |
| GIGABYTE | Z590 UD AC                          |            | N            | U            | N            | N            |
| GIGABYTE | Z590 VISION D                       |            | N            | U            | N            | N            |
| GIGABYTE | Z590 VISION G                       |            | N            | U            | N            | N            |
| ASUS     | Z590 WIFI GUNDAM EDITION            | NCT6798D   | N            | N            | Y            | N            |
| GIGABYTE | Z690M AORUS ELITE AX DDR4           |            | N            | Y            | N            | N            |
| ASROCK   | Z87 Extreme6                        |            | N            | N            | N            | N            |
| ASROCK   | Z87 Pro3                            |            | N            | N            | N            | N            |
| GIGABYTE | Z97-HD3                             |            | N            | N            | N            | N            |
| ASUS     | Z97-PRO GAMER                       | NCT5538D   | N            | N            | N            | N            |

* L - no DSDL/SSDL dumps,
* F - can't unpack UEFI capsule,
* N - unsupported,
* Y - supported and upstreamed,
* U - to upstream,
* ? - upstreamed but not detected by script,
* M - required method exists, port defined in different way,
* W - required method exists, no wmi method defined,
* P - return zero, no valid sensors results or requires custom lock.

Notes:
* Some boards are used nct6799 sensor and
  [additional patch](https://patchwork.kernel.org/project/linux-hwmon/patch/20221228135744.281752-1-linux@roeck-us.net/)
  apply is requited.
* IT8665E like sensors required custom it87 module and WMI proxy implementation,
  that is not implemeted for now.

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
