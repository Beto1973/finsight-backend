export interface BacktestPoint {
  date: string;
  portfolioValue: number;
}

export interface BacktestResult {
  series: BacktestPoint[];
  totalReturn: number;
  maxDrawdown: number;
}

export function runPortfolioBacktest(
  prices: Record<string, number[]>,
  weights: Record<string, number>
): BacktestResult {
  const length = Math.min(
    ...Object.values(prices).map((p) => p.length)
  );

  const series: BacktestPoint[] = [];
  let peak = 0;

  for (let i = 0; i < length; i++) {
    let value = 0;

    for (const ticker in prices) {
      value += prices[ticker][i] * weights[ticker];
    }

    peak = Math.max(peak, value);

    series.push({
      date: `T-${length - i}`,
      portfolioValue: value,
    });
  }

  const start = series[0].portfolioValue;
  const end = series[series.length - 1].portfolioValue;

  const maxDrawdown = Math.min(
    ...series.map((p) => (p.portfolioValue - peak) / peak)
  );

  return {
    series,
    totalReturn: (end - start) / start,
    maxDrawdown,
  };
}
