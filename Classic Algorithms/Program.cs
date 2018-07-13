using System;
using System.Collections.Generic;

namespace Classic_Algorithms
{
    class Program
    {
        static void Main(string[] args)
        {
            try {
                //Collatz Conjecture test
                int count1 = CollatzConjecture.Calculate(6);
                Console.WriteLine("Collatz Conjecture for 6: " + count1);
                
                int count2 = CollatzConjecture.Calculate(9);
                Console.WriteLine("Collatz Conjecture for 9: " + count2);

                //Sorting test
                List<int> test1 = new List<int>() { 5, 6, 1, 3, 9, 4 };
                List<int> result1 = Sorting.BubbleSort(test1);
                Sorting.Print(result1);

                List<int> test2 = new List<int>() { 5, 6, 1, 3, 9, 4 };
                List<int> result2 = Sorting.MergeSort(test2);
                Sorting.Print(result2);

                //Closest Pair test
                List<Position> points = new List<Position>();
                points.Add(new Position(2.3,56));
                points.Add(new Position(5,9.6));
                points.Add(new Position(-78,61));
                points.Add(new Position(-23,-6.4));
                points.Add(new Position(4.5,-9.8));

                Position p11, p12;
                double distance1;
                (p11, p12, distance1) = ClosestPair.Calculate(points, DistanceMetric.EuclideanDistance);
                ClosestPair.Print(p11,p12,distance1, DistanceMetric.EuclideanDistance);

                Position p21, p22;
                double distance2;
                (p21, p22, distance2) = ClosestPair.Calculate(points, DistanceMetric.MeanAbsoluteError);
                ClosestPair.Print(p21,p22,distance2, DistanceMetric.MeanAbsoluteError);

                Position p31, p32;
                double distance3;
                (p31, p32, distance3) = ClosestPair.Calculate(points, DistanceMetric.MeanSquaredError);
                ClosestPair.Print(p31,p32,distance3, DistanceMetric.MeanSquaredError);

                Position p41, p42;
                double distance4;
                (p41, p42, distance4) = ClosestPair.Calculate(points, DistanceMetric.SumOfAbsoluteDistance);
                ClosestPair.Print(p41,p42,distance4, DistanceMetric.SumOfAbsoluteDistance);

                Position p51, p52;
                double distance5;
                (p51, p52, distance5) = ClosestPair.Calculate(points, DistanceMetric.SumOfSquaredDifference);
                ClosestPair.Print(p51,p52,distance5, DistanceMetric.SumOfSquaredDifference);


            } catch(Exception e) {
                Console.WriteLine(e.Message);
                Console.WriteLine(e.StackTrace);
            }
        }
    }
}
