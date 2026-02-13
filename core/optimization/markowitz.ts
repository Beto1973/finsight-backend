export interface OptimizationInput {
  expectedReturns: Record<string, number>;
  covariance: number[][];
  tickers: string[];
  maxWeight?: number;
}

export interface OptimizationResult {
  weights: Record<string, number>;
}

export function optimizeMarkowitz(
  input: OptimizationInput
): OptimizationResult {
  const n = input.tickers.length;
  const equalWeight = 1 / n;

  const weights: Record<string, number> = {};

  input.tickers.forEach((t) => {
    weights[t] = Math.min(
      equalWeight,
      input.maxWeight ?? equalWeight
    );
  });

  return { weights };
}
