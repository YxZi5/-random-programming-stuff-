Antimalware Scan Interface (AMSI) Bypass. This bypass works by load amsi.dll library into own process memory and find address of 'AmsiScanBuffer' function.
Next amsiBypass overwrite 'AmsiScanBuffer' with this bytes: '0xB8, 0x57, 0x00, 0x07, 0x80, 0xC3' - always AMSI_RESULT_CLEAN which indicates that no detection has been found.

This bypass using 'Caesar cipher' with key 15 (decimal) to encrypt strings.This cipher are implemented inside of amsi_b.cpp in function 'decryptCaesarCipher' this function takes two parameters encrypted string and key, function returns decrypted string as string obviously.
