import math

# -------------------------------
# Base Class (Inheritance Example)
# -------------------------------
class PetroleumProblem:
    def solve(self):
        raise NotImplementedError("Each problem must implement solve()")


# -------------------------------
# 1. Hydrostatic Pressure
# -------------------------------
class HydrostaticPressure(PetroleumProblem):
    def __init__(self, density, depth):
        self.density = density  # ppg
        self.depth = depth      # ft

    def solve(self):
        try:
            pressure = 0.052 * self.density * self.depth  # psi
            return f"Hydrostatic Pressure: {pressure:.2f} psi"
        except Exception as e:
            return f"Error: {e}"


# -------------------------------
# 2. Gas Formation Volume Factor
# -------------------------------
class GasFVF(PetroleumProblem):
    def __init__(self, z, T, P):
        self.z = z  # compressibility factor
        self.T = T  # Rankine
        self.P = P  # psia

    def solve(self):
        try:
            Bg = 0.02827 * self.z * self.T / self.P  # res ft3/scf
            return f"Gas FVF (Bg): {Bg:.5f} res ft³/scf"
        except Exception as e:
            return f"Error: {e}"


# -------------------------------
# 3. Darcy Flow Rate
# -------------------------------
class DarcyFlow(PetroleumProblem):
    def __init__(self, k, h, dp, mu, L):
        self.k = k   # md
        self.h = h   # ft
        self.dp = dp # psi
        self.mu = mu # cp
        self.L = L   # ft

    def solve(self):
        try:
            q = (0.001127 * self.k * self.h * self.dp) / (self.mu * self.L)
            return f"Darcy Flow Rate: {q:.2f} STB/day"
        except Exception as e:
            return f"Error: {e}"


# -------------------------------
# 4. Pump Factor
# -------------------------------
class PumpFactor(PetroleumProblem):
    def __init__(self, D, rod, stroke, eff):
        self.D = D        # liner dia, in
        self.rod = rod    # rod dia, in
        self.stroke = stroke  # in
        self.eff = eff/100    # efficiency fraction

    def solve(self):
        try:
            area = (math.pi/4) * ((self.D**2) - (self.rod**2))
            V = area * self.stroke / 231  # barrels per stroke
            return f"Pump Factor: {(V * self.eff):.4f} bbl/stroke"
        except Exception as e:
            return f"Error: {e}"


# -------------------------------
# 5. Oil Initially In Place (OOIP)
# -------------------------------
class ReservoirOOIP(PetroleumProblem):
    def __init__(self, A, h, phi, Soi, Bo):
        self.A = A      # acres
        self.h = h      # ft
        self.phi = phi  # porosity fraction
        self.Soi = Soi  # oil saturation fraction
        self.Bo = Bo    # bbl/STB

    def solve(self):
        try:
            OOIP = (7758 * self.A * self.h * self.phi * self.Soi) / self.Bo
            return f"OOIP: {OOIP:.2f} STB"
        except Exception as e:
            return f"Error: {e}"


# -------------------------------
# 6. Bubble Point Check
# -------------------------------
class BubblePoint(PetroleumProblem):
    def __init__(self, Pb, P):
        self.Pb = Pb  # bubble point pressure
        self.P = P    # reservoir pressure

    def solve(self):
        try:
            if self.P > self.Pb:
                return "Reservoir pressure is above bubble point"
            else:
                return "Reservoir pressure is below bubble point"
        except Exception as e:
            return f"Error: {e}"


# -------------------------------
# Function to run all problems
# -------------------------------
def run_all():
    problems = [
        HydrostaticPressure(10, 10000),
        GasFVF(0.9, 520, 3000),
        DarcyFlow(50, 30, 100, 1.2, 500),
        PumpFactor(6.5, 2.5, 18, 80),
        ReservoirOOIP(640, 30, 0.20, 0.75, 1.25),
        BubblePoint(2500, 3000)
    ]

    for p in problems:
        print(p.solve())


# -------------------------------
# Main Program (Error Catching)
# -------------------------------
if __name__ == "__main__":
    try:
        run_all()
    except Exception as e:
        print(f"Unexpected Error: {e}")
