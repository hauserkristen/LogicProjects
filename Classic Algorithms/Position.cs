namespace Classic_Algorithms
{
    public class Position
    {
        private double _x;
        private double _y;

        public Position(double x, double y) {
            _x = x;
            _y = y;
        }

        public double X {
            get {
                return _x;
            }
            set {
                _x = value;
            }
        }

        public double Y {
            get {
                return _y;
            }
            set {
                _y = value;
            }
        }

    }
}