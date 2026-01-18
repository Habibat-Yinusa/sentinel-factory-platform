flowchart TD
    Client[Client / Frontend<br>(Postman, Browser)] --> API[FastAPI API Layer<br>/machines, /telemetry, /incidents, /audit]
    API --> Domain[Domain Layer<br>Machine, Telemetry, Incident, Audit]
    Domain --> DB[SQLite Database<br>(machines, telemetry, incidents)]

    %% Optional: illustrate flows
    subgraph TelemetryFlow["Telemetry Flow"]
        API -->|Submit telemetry| Domain
        Domain -->|Store readings| DB
        Domain -->|Check for incidents| DB
    end

    subgraph AuditFlow["Audit Flow"]
        API -->|Request trends| Domain
        Domain -->|Read telemetry & incidents| DB
        Domain -->|Return report| API
    end
