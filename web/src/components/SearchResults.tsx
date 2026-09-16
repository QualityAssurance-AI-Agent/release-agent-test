import React from "react";

export interface Payment {
  id: string;
  amountMinor: number;
  currency: string;
  status: "pending" | "settled" | "failed";
}

export function formatAmount(amountMinor: number, currency: string): string {
  return `${(amountMinor / 100).toFixed(2)} ${currency}`;
}

export function SearchResults({ payments }: { payments: Payment[] }) {
  if (payments.length === 0) {
    return <p className="empty">No payments matched your search.</p>;
  }
  return (
    <ul className="results">
      {payments.map((payment) => (
        <li key={payment.id} className={`result result--${payment.status}`}>
          <span className="result__id">{payment.id}</span>
          <span className="result__amount">
            {formatAmount(payment.amountMinor, payment.currency)}
          </span>
          <span className="result__status">{payment.status}</span>
        </li>
      ))}
    </ul>
  );
}
