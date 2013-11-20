This is tested with WebLogic 10.3.5, 10.3.6.
- Don't forget to delete produced plan after rerun
- Looks that password in the original jdbc definition has to be 
encrypted using the same algorithm as the new one, 3DES or AES
- Also note that WLS console does not properly reflect deployment
plan changes. The fix for 10.3.6 is available as patch for bug 17199498
