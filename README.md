# asus-board-dsdt

Collection of DSDT files required for support of https://bugzilla.kernel.org/show_bug.cgi?id=204807

All files are provided by motherboard users or downloaded and extracted from support section of ASUS website.

# Required code samples for nct6775 support (B550 based)

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
