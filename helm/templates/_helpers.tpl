{{- define "frontend.labels" -}}
app: {{ .Chart.Name }}
component: frontend
{{- end -}}

{{- define "backend.labels" -}}
app: {{ .Chart.Name }}
component: backend
{{- end -}}