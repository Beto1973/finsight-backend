/* =============================
   TYPE DEFINITIONS (DECOUPLED)
   ============================= */

export interface CommitteeAssetSummary {
  ticker: string;
  scoring: {
    total_score: number;
  };
  alerts: any[];
}

export interface AllocationResult {
  ticker: string;
  weight: number;
  score: number;
}

export interface PortfolioDecisionResult {
  decision: string;
  score: number;
  rationale: string;
}

export interface CommitteeReportInput {
  portfolio: CommitteeAssetSummary[];
  allocation: AllocationResult[];
  decision: PortfolioDecisionResult;
  generatedAt: string;
}

/* =============================
   REPORT BUILDER
   ============================= */

export function buildCommitteeReportText(
  input: CommitteeReportInput
): string {
  const lines: string[] = [];

  lines.push("INVESTMENT COMMITTEE REPORT");
  lines.push(`Generated at: ${input.generatedAt}`);
  lines.push("");

  lines.push(`PORTFOLIO DECISION: ${input.decision.decision}`);
  lines.push(`Aggregate Score: ${input.decision.score}`);
  lines.push("");

  lines.push("RATIONALE:");
  lines.push(input.decision.rationale);
  lines.push("");

  lines.push("CAPITAL ALLOCATION:");
  input.allocation.forEach((a) => {
    lines.push(
      `- ${a.ticker}: ${(a.weight * 100).toFixed(1)}% (Score ${a.score})`
    );
  });

  lines.push("");
  lines.push("ASSET SUMMARY:");
  input.portfolio.forEach((p) => {
    lines.push(
      `- ${p.ticker}: ${p.scoring.total_score} | Alerts: ${p.alerts.length}`
    );
  });

  return lines.join("\n");
}

