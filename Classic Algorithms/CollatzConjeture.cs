using System;

namespace Classic_Algorithms
{
    public class CollatzConjecture
    {
        public static int Calculate(int initialValue) 
        {
            int count = 0;

            if (initialValue == 1)
            {
                throw new ArgumentOutOfRangeException("Initial value must be greater than 1.");
            }

            while(initialValue != 1)
            {
                if (initialValue % 2 == 0) 
                {
                    initialValue /= 2;
                }
                else 
                {
                    initialValue *= 3;
                    initialValue += 1;
                }

                count++;
            }

            return count;
        }
    }
}
