import lib601.sig as sig
import lib601.poly as poly

step1 = sig.Rn(3.0 * sig.StepSignal(), 3)

step2 = sig.Rn(-3.0 * sig.StepSignal(), 7)

stepUpDown = sig.SummedSignal(step1, step2)

stepDownPoly = sig.polyR(sig.UnitSampleSignal, poly.Polynomial([1, 0, 3, 0, 5, 0]))
