using System;

namespace Classic_Algorithms
{
    public enum DistanceMetric {
        SumOfAbsoluteDistance,
        SumOfSquaredDifference,
        MeanAbsoluteError,
        MeanSquaredError,
        EuclideanDistance
    }

    public class DistanceMetricFunctions
    {
        public static double SumOfAbsoluteDistance(Position first, Position second) {
            return Math.Abs(first.X - second.X) + Math.Abs(first.Y - second.Y);
        }

        public static double SumOfSquaredDifference(Position first, Position second) {
            return Math.Pow(first.X - second.X, 2) + Math.Pow(first.Y - second.Y, 2);
        }

        public static double MeanAbsoluteError(Position first, Position second) {
            double sum = SumOfAbsoluteDistance(first, second);
            return sum / 2.0;
        }

        public static double MeanSquaredError(Position first, Position second) {
            double sum = SumOfSquaredDifference(first, second);
            return sum / 2.0;
        }

        public static double EuclideanDistance(Position first, Position second) {
            double sum = SumOfSquaredDifference(first, second);
            return Math.Sqrt(sum);
        }
    }
}
