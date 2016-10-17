bool isPowerOfTwo(int n) {
  if (n<=0) {
    return false;
  }
  for(;;){
    if (n&1) {
      n = n>>1;
      break;
    }
    n = n>>1;
  }
  if (n) {
    return false;
  }
  return true;
}
