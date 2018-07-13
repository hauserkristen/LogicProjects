using System;
using System.Collections.Generic;

namespace Classic_Algorithms
{
    public class Sorting
    {
        public static List<T> BubbleSort<T>(List<T> list) where T : IComparable<T> {
            int n = list.Count;
            for (int i = 0; i < n - 1; i++) {
                for (int j = 0; j < n - i - 1; j++) {
                    if (list[j].CompareTo(list[j + 1]) > 0) {
                        //Swap entities
                        T temp = list[j];
                        list[j] = list[j + 1];
                        list[j + 1] = temp;
                    }
                }
            }

            return list;
        }

        public static List<T> MergeSort<T>(List<T> list) where T : IComparable<T> {
            if (list.Count > 1) {
                int middle = list.Count / 2;

                //Split list in half
                List<T> left = new List<T>();
                List<T> right = new List<T>();
                for(int n = 0; n < list.Count; n++) {
                    if (n < middle) {
                        left.Add(list[n]);
                    } else {
                        right.Add(list[n]);
                    }
                }

                //Recurse
                List<T> sortedLeft = MergeSort(left);
                List<T> sortedRight = MergeSort(right);

                //Merge the lists
                List<T> finalList = new List<T>(list);
                int i = 0, j = 0, k = 0;
                while (i < sortedLeft.Count && j < sortedRight.Count) {
                    if (sortedLeft[i].CompareTo(sortedRight[j]) < 0) {
                        finalList[k] = sortedLeft[i];
                        i++;
                    } else {
                        finalList[k] = sortedRight[j];
                        j++;
                    }
                    k += 1;
                }

                while (i < sortedLeft.Count) {
                    finalList[k] = sortedLeft[i];
                    i++;
                    k++;
                }

                while (j < sortedRight.Count) {
                    finalList[k] = sortedRight[j];
                    j++;
                    k++;
                }

                return finalList;
            } else {
                return list;
            }
        }

    
        public static void Print<T>(List<T> list) {

            Console.Write("Sorted List: ");
            for (int i = 0; i < list.Count; i ++) {
                Console.Write(list[i] + " ");
            }
            Console.WriteLine();
        }
    }
}
