void GetNext(char* p,int next[])
{
    next[0] = -1;
    int k = -1;
    int j = 0;
    while (p[j+1]!='\0')
    {
        if (k == -1 || p[j] == p[k])
        {
            ++k;
            ++j;
            next[j] = k;
        }
        else
        {
            k = next[k];
        }
    }
}
int strStr(char* haystack, char* needle) {
  int i = 0;
  int j = 0;
  int pLen = strlen(needle);
  int * next = (int *)malloc(pLen*sizeof(int));
  GetNext(needle, next);
  while (haystack[i] != '\0' && j < pLen)
  {
      if (j == -1 || haystack[i] == needle[j])
      {
          i++;
          j++;
      }
      else
      {
          j = next[j];
      }
  }
  if (j == pLen)
      return i - j;
  else
      return -1;
}
