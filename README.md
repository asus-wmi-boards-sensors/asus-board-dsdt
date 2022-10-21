# asus-board-dsdt

Collection of DSDT files required for support of https://bugzilla.kernel.org/show_bug.cgi?id=204807

All files are provided by motherboard users or downloaded and extracted from support section of ASUS website.

[How it works](https://bugzilla.kernel.org/show_bug.cgi?id=204807#c37)

# Supported boards

| board                            | asus_wmi_sensors | nct6777 | asus_ec_sensors |
| -------------------------------- | ---------------- | ------- | --------------- |
| CROSSHAIR VI HERO                | Y                | N       | N               |
| MAXIMUS VII HERO                 | N                | P       | N               |
| P8H67                            | N                | P       | N               |
| P8Z68-V LX                       | N                | P       | N               |
| PRIME B360-PLUS                  | N                | Y       | N               |
| PRIME B450M-GAMING               | N                | P       | N               |
| PRIME B460-PLUS                  | N                | Y       | N               |
| PRIME B550M-A                    | N                | Y       | N               |
| PRIME B550M-A (WI-FI)            | N                | Y       | N               |
| PRIME B550-PLUS                  | N                | Y       | N               |
| PRIME H410M-R                    | N                | Y       | N               |
| PRIME X370-PRO                   | N                | P       | N               |
| PRIME X399-A                     | Y                | P       | N               |
| PRIME X470-PRO                   | Y                | P       | N               |
| PRIME X570-P                     | N                | Y       | N               |
| PRIME X570-PRO                   | N                | Y       | Y               |
| PRIME Z270-A                     | N                | P       | N               |
| PRIME Z370-A                     | N                | P       | N               |
| ProArt X570-CREATOR WIFI         | N                | Y       | Y               |
| Pro B550M-C                      | N                | Y       | N               |
| PRO H410T                        | N                | Y       | N               |
| Pro WS X570-ACE                  | N                | Y       | Y               |
| ROG CROSSHAIR VI EXTREME         | Y                | N       | N               |
| ROG CROSSHAIR VI Hero            | N                | P       | N               |
| ROG CROSSHAIR VI HERO (WI-FI AC) | Y                | N       | N               |
| ROG CROSSHAIR VII HERO (WI-FI)   | Y                | N       | N               |
| ROG CROSSHAIR VII HERO           | Y                | N       | N               |
| ROG CROSSHAIR VIII DARK HERO     | N                | Y       | Y               |
| ROG CROSSHAIR VIII FORMULA       | N                | Y       | Y               |
| ROG CROSSHAIR VIII HERO          | N                | Y       | Y               |
| ROG CROSSHAIR VIII HERO (WI-FI)  | N                | N       | Y               |
| ROG CROSSHAIR VIII IMPACT        | N                | Y       | Y               |
| ROG MAXIMUS X HERO               | N                | P       | N               |
| ROG MAXIMUS XI HERO              | N                | N       | Y               |
| ROG MAXIMUS XI HERO (WI-FI)      | N                | N       | Y               |
| ROG STRIX B350-F GAMING          | N                | P       | N               |
| ROG STRIX B450-E GAMING          | Y                | N       | N               |
| ROG STRIX B450-F GAMING II       | Y                | N       | N               |
| ROG STRIX B450-F GAMING          | Y                | P       | N               |
| ROG STRIX B450-I GAMING          | Y                | N       | N               |
| ROG STRIX B550-A GAMING          | N                | Y       | N               |
| ROG STRIX B550-E GAMING          | N                | Y       | Y               |
| ROG STRIX B550-F GAMING          | N                | Y       | N               |
| ROG STRIX B550-F GAMING WIFI II  | N                | Y       | N               |
| ROG STRIX B550-F GAMING (WI-FI)  | N                | Y       | N               |
| ROG STRIX B550-I GAMING          | N                | Y       | Y               |
| ROG STRIX B550-XE GAMING (WI-FI) | N                | Y       | N               |
| ROG STRIX X399-E GAMING          | Y                | P       | N               |
| ROG STRIX X470-F GAMING          | Y                | N       | N               |
| ROG STRIX X470-I GAMING          | Y                | N       | N               |
| ROG STRIX X570-E GAMING          | N                | Y       | Y               |
| ROG STRIX X570-E GAMING WIFI II  | N                | Y       | Y               |
| ROG STRIX X570-F GAMING          | N                | Y       | Y               |
| ROG STRIX X570-I GAMING          | N                | Y       | Y               |
| ROG STRIX X670E-I GAMING WIFI    | N                | P       | N               |
| ROG STRIX Z270-E                 | N                | P       | N               |
| ROG STRIX Z370-E                 | N                | P       | N               |
| ROG STRIX Z370-H GAMING          | N                | P       | N               |
| ROG STRIX Z390-E GAMING          | N                | Y       | N               |
| ROG STRIX Z390-F GAMING          | N                | Y       | N               |
| ROG STRIX Z390-H GAMING          | N                | Y       | N               |
| ROG STRIX Z390-I GAMING          | N                | Y       | N               |
| ROG STRIX Z490-A GAMING          | N                | Y       | N               |
| ROG STRIX Z490-E GAMING          | N                | Y       | N               |
| ROG STRIX Z490-F GAMING          | N                | Y       | N               |
| ROG STRIX Z490-F                 | N                | P       | N               |
| ROG STRIX Z490-G GAMING          | N                | Y       | N               |
| ROG STRIX Z490-G GAMING (WI-FI)  | N                | Y       | N               |
| ROG STRIX Z490-H GAMING          | N                | Y       | N               |
| ROG STRIX Z490-I GAMING          | N                | Y       | N               |
| ROG STRIX Z690-A GAMING WIFI D4  | N                | N       | Y               |
| ROG ZENITH EXTREME ALPHA         | Y                | N       | N               |
| ROG ZENITH EXTREME               | Y                | N       | N               |
| ROG ZENITH II EXTREME            | N                | N       | Y               |
| TUF B450 PLUS GAMING             | N                | P       | N               |
| TUF GAMING B550M-PLUS            | N                | Y       | N               |
| TUF GAMING B550M-PLUS (WI-FI)    | N                | Y       | N               |
| TUF GAMING B550-PLUS             | N                | Y       | N               |
| TUF GAMING B550-PLUS WIFI II     | N                | Y       | N               |
| TUF GAMING B550-PRO              | N                | Y       | N               |
| TUF GAMING X570-PLUS             | N                | Y       | N               |
| TUF GAMING X570-PLUS (WI-FI)     | N                | Y       | N               |
| TUF GAMING X570-PRO (WI-FI)      | N                | Y       | N               |
| TUF GAMING Z490-PLUS             | N                | Y       | N               |
| TUF GAMING Z490-PLUS (WI-FI)     | N                | Y       | N               |
| Z170-DELUXE                      | N                | P       | N               |
| Z170M-PLUS                       | N                | P       | N               |

* N - unsupported,
* Y - supported,
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

# Required code samples for asus_wmi_ec_sensors boards support (`ROG STRIX X570-E GAMING` based)

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
	uint8_t	guid[16];			/* GUID */
	union {
		uint8_t 	obj_id[2];	/* Object Identifier */
		struct {
			uint8_t	notify_id;	/* Notify Identifier */
			uint8_t	reserved;	/* Reserved */
		} notify;
	} id;
	uint8_t	instance;			/* Instance */
	uint8_t	flags;				/* fwts_wmi_flags */
} __attribute__ ((packed)) fwts_wdg_info;
```
