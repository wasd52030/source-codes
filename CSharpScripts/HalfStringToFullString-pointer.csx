Console.WriteLine("Hello, World!".halfToFull());

unsafe static string halfToFull(this string input) {
  fixed(char * p = input) {
    for (int i = 0; i < input.Length; i++) {
      var ptr = p + i;
      if ( * ptr == 32) {
        * ptr = (char) 12288;
      } else if ( * ptr > 32 && * ptr < 127) {
        * ptr += (char) 65248;
      }
    }
  }
  return input;
}