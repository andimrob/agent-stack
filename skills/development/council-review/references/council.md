# The council

Eight members sit on the council. Each one proposes findings only inside its own
remit. Each one votes on every finding, its own and its peers', as a senior
engineer who asks three questions:

- **Real?** The cited code does what the finding claims. You read it yourself.
- **In scope?** This PR introduced or changed it. A pre-existing problem the PR did
  not touch is out of scope.
- **Worth a comment?** A senior reviewer would stop the author for it. A linter,
  formatter, or type checker would not already catch it.

Brief each member with its own section below, plus the shared questions above.

## Security

**Looks for**: missing or weakened authentication and authorization checks;
injection (SQL, shell, template, path traversal, XSS); secrets in code, logs, or
config; unsafe deserialization; SSRF; open redirects; mass assignment; PII or
credentials that reach logs, analytics, error reports, or URLs; new dependencies
with known advisories.

**Evidence bar**: a concrete attack vector through code in this PR. "An attacker
might somehow…" without a path from input to impact is not a finding.

**Leaves to others**: general error handling (Correctness), logging volume
(Observability).

## Correctness

**Looks for**: logic errors; off-by-one; wrong conditions; null, empty, and
missing-key handling; error paths that swallow or mask failures; races and
non-atomic read-modify-write; time zones and money arithmetic; transactions that
can half-apply; callers in the call-site map that the change breaks (new return
shape, new exception, new side effect, changed argument meaning); persisted data,
caches, queues, or schemas that still hold the old shape.

**Evidence bar**: an input or state, and the wrong result it produces.

**Leaves to others**: whether a test covers the bug (Testing), structure of the fix
(Design).

## Testing

**Looks for**: changed behaviour with no test; tests that cannot fail (assert on a
mock they set up, assert nothing, or catch the error they test for); tests that
pin implementation details instead of behaviour; missing edge and failure cases
for the paths Correctness cares about; fakes that drift from the real interface;
order-dependent, time-dependent, or network-dependent tests; deleted or skipped
tests with no reason in the PR.

**Evidence bar**: the behaviour that a test does not protect, and the bug that
would pass unnoticed.

**Leaves to others**: test style and naming that a linter enforces.

## Architecture

**Looks for**: changes that cross a module, service, or layer boundary; new
coupling or a dependency that points the wrong way; a new pattern where the
codebase already has an established one for the same job; logic placed in the
wrong layer (domain logic in a controller, I/O in a model); shared state; changes
that make a later migration or extraction harder; contracts with other services
changed without a version or a compatibility path.

**Evidence bar**: the existing pattern or boundary, with a path, and how this PR
departs from it.

**Leaves to others**: names and interface shape inside one module (Design).

## Design

**Looks for**: interface and API shape (parameters, return values, error
contracts); shallow modules that add an interface without hiding complexity;
names that mislead; duplication of logic that already exists in the codebase;
dead code, speculative generality, and flags that only one caller uses; public
surface wider than the callers need; code a new reader cannot follow without the
PR description.

**Evidence bar**: the confusion or change cost the design causes, with the caller
or reader who pays it.

**Leaves to others**: cross-module structure (Architecture), lint-level style.

## Performance

**Looks for**: N+1 queries; queries without a usable index; unbounded loads
(no limit, no pagination, whole table into memory); work inside loops that can
move out; synchronous network or disk I/O on a request path; missing timeouts;
hot-path allocations; caches with no bound or no invalidation; algorithmic
complexity that grows with user data.

**Evidence bar**: the path, the input size that makes it slow, and why that size
is realistic.

**Leaves to others**: micro-optimisations with no measured or obvious cost.

## Observability

**Looks for**: new failure modes nobody will see (rescued and dropped errors, no
error report, no log); logs without the identifiers needed to trace a request;
logs that are too noisy for production; new jobs, endpoints, or integrations with
no metric, trace, or alert; metric names or tags with unbounded cardinality;
changes that break an existing dashboard, monitor, or alert query; health checks
that no longer reflect health.

**Evidence bar**: the production incident in which an on-call engineer could not
tell what happened.

**Leaves to others**: secrets or PII in logs (Security).

## Analytics

**Looks for**: user-facing behaviour that adds, removes, or changes a tracked
event; event names, properties, or types changed without a migration for
downstream consumers; schema or column changes that warehouse, ETL, or reporting
jobs read; experiment and feature-flag assignment or exposure logging that is
missing or now fires at the wrong time; double counting or dropped events on
retries; data retention or consent rules that the new data ignores.

**Evidence bar**: the downstream consumer, report, or decision that will get
wrong or missing data.

**Leaves to others**: PII exposure (Security), application logs (Observability).
