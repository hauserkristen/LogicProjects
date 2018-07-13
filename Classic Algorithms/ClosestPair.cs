using System;
using System.Collections.Generic;

namespace Classic_Algorithms
{
    public class ClosestPair
    {
        
        public static (Position, Position, double) Calculate(List<Position> points, DistanceMetric metric) {
            Position closestA = null, closestB = null;
            double minDistance = double.MaxValue;

            for(int i = 0; i < points.Count-1; i++) {
                for(int j = i + 1; j < points.Count; j++){
                    Position point1 = points[i];
                    Position point2 = points[j];

                    double distance;
                    switch(metric) {
                        case DistanceMetric.EuclideanDistance:
                            distance = DistanceMetricFunctions.EuclideanDistance(point1, point2);
                            break;
                        case DistanceMetric.MeanAbsoluteError:
                            distance = DistanceMetricFunctions.MeanAbsoluteError(point1, point2);
                            break;
                        case DistanceMetric.MeanSquaredError:
                            distance = DistanceMetricFunctions.MeanSquaredError(point1, point2);
                            break;
                        case DistanceMetric.SumOfAbsoluteDistance:
                            distance = DistanceMetricFunctions.SumOfAbsoluteDistance(point1, point2);
                            break;
                        case DistanceMetric.SumOfSquaredDifference:
                            distance = DistanceMetricFunctions.SumOfSquaredDifference(point1, point2);
                            break;
                        default:
                            throw new NotSupportedException("Metric type not supported");
                    }

                    if (distance < minDistance) {
                        closestA = point1;
                        closestB = point2;
                        minDistance = distance;
                    }

                }
            }

            return (closestA, closestB, minDistance);
        }

        public static void Print(Position first, Position second, double distance, DistanceMetric metric){
            Console.WriteLine("--------------------------------");
            Console.WriteLine("Distance Metric: " + metric.ToString());
            Console.WriteLine("Point 1: (" + first.X + "," + first.Y + ")");
            Console.WriteLine("Point 2: (" + second.X + "," + second.Y + ")");
            Console.WriteLine("Distance: " + distance);
            Console.WriteLine("--------------------------------");
        }

    }
}