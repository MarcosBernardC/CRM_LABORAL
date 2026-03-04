-- WARNING: This schema is for context only and is not meant to be run.
-- Table order and constraints may not be valid for execution.

CREATE TABLE public.postulaciones (
  id uuid NOT NULL DEFAULT gen_random_uuid(),
  fecha_postulacion date DEFAULT CURRENT_DATE,
  empresa text NOT NULL,
  puesto text NOT NULL,
  plataforma text DEFAULT 'Computrabajo'::text,
  estado text DEFAULT 'Enviada'::text,
  url_vacante text,
  modalidad text,
  proyecto_detalle text,
  stack_tecnico jsonb,
  estrategia_completa jsonb,
  notas_adicionales jsonb,
  prioridad text DEFAULT 'Media'::text,
  cliente_sector text,
  verificado text,
  created_at timestamp with time zone NOT NULL DEFAULT timezone('utc'::text, now()),
  CONSTRAINT postulaciones_pkey PRIMARY KEY (id)
);