<img align="right" src="assets/logo_hex_mse.svg" alt="Logo de Evaluación de Estrategias de Manejo" width="110">

# Fisheries MSE<br>Template

Plantilla reproducible para estructurar proyectos de **Management Strategy Evaluation (MSE)** en pesquerías, desde los objetivos de manejo y la evidencia hasta la simulación de ciclo cerrado, evaluación de desempeño, documentación y certificación.

<br clear="right">

> **Idioma principal:** español. [English version](README.en.md) · [Mapa completo del repositorio](REPOSITORY_MAP.md)

## Qué es este repositorio

Este repositorio es un **`type-template`** público y reutilizable. No representa una MSE ya resuelta, una especie real ni un artículo científico concreto. Su función es proporcionar una estructura común, trazable y reproducible para iniciar proyectos MSE aplicados a una especie, stock o pesquería.

Por defecto, un repositorio creado mediante **Use this template** debe clasificarse como **`type-project`**, porque representa un proyecto científico aplicado que puede producir posteriormente papers, workflows, reportes, software u otros outputs. Si el repositorio generado tiene otro propósito real, su clasificación debe ajustarse explícitamente.

## Qué problema resuelve

Una MSE no consiste únicamente en seleccionar una cuota o una regla de control de captura. Debe evaluar si un procedimiento de manejo sigue cumpliendo objetivos definidos bajo incertidumbre biológica, pesquera, observacional, de evaluación e implementación.

El ciclo conceptual es:

`objetivos de manejo -> sistema biológico y pesquero -> modelo operativo -> observaciones simuladas -> evaluación o indicador -> procedimiento de manejo -> implementación -> respuesta del sistema -> métricas de desempeño -> comparación de alternativas`

Después de seleccionar una estrategia, el proceso continúa con seguimiento, revisión periódica y protocolos para circunstancias excepcionales.

## Alcance científico

La plantilla cubre, de forma modular:

- gobernanza, objetivos de manejo y tolerancias de riesgo;
- biología, ecología, pesquería, monitoreo y evaluación de stock;
- diseño y condicionamiento del Operating Model;
- Observation Model y Estimation Model;
- Management Procedures y reglas de control;
- Implementation Model;
- escenarios de incertidumbre;
- simulación de ciclo cerrado;
- métricas de desempeño y trade-offs;
- seguimiento, circunstancias excepcionales y revisión;
- trazabilidad, reporting y certificación de configuraciones y corridas.

El template no prescribe mortalidad natural, crecimiento, reclutamiento, estructura espacial, modelo de evaluación, puntos de referencia ni HCR específicos. Esos elementos deben definirse para cada caso con evidencia o mediante decisiones científicas documentadas.

## Uso del template

1. Crear un repositorio nuevo mediante **Use this template**.
2. Reemplazar inmediatamente la identidad heredada en `repo.yml` por el nombre, título, visibilidad, estado y clasificación del nuevo proyecto.
3. Completar `species_profile.yml` con el caso de estudio real.
4. Revisar `publication.yml`, `DATA_POLICY.md` y las restricciones institucionales antes de añadir datos.
5. Definir objetivos y tolerancias de riesgo antes de diseñar procedimientos de manejo.
6. Registrar fuentes, datos, parámetros y decisiones en `references/` y `registry/`.
7. Mantener como `TBD` cualquier elemento que aún no tenga evidencia o una decisión formal.

Consulte [`TEMPLATE_USAGE.md`](TEMPLATE_USAGE.md) para la guía de inicio y [`REPOSITORY_MAP.md`](REPOSITORY_MAP.md) para navegar la estructura completa.

## Arquitectura del repositorio

| Carpeta | Función |
|---|---|
| `.github/` | Automatización, plantillas de issues y revisión en GitHub. |
| `assets/` | Recursos gráficos e identidad visual. |
| `docs/` | Documentación científica, de gobernanza y decisiones. |
| `data/` | Datos separados por nivel de acceso y etapa de procesamiento. |
| `references/` | Literatura, normas e informes que sustentan decisiones. |
| `registry/` | Registros maestros de fuentes, datos, parámetros, escenarios, decisiones y corridas. |
| `config/` | Configuración concreta de modelos, escenarios y procedimientos. |
| `models/` | Especificaciones conceptuales de los componentes del MSE. |
| `src/` | Funciones reutilizables. |
| `scripts/` | Orquestación de etapas del workflow. |
| `tests/` | Estructura reservada para pruebas unitarias, de integración, regresión y validación científica del proyecto generado. |
| `reports/` | Fuentes reproducibles de informes y productos de comunicación. |
| `outputs/` | Resultados generados; se ignoran por defecto salvo documentación explícitamente versionada. |
| `certification/` | Configuraciones y artefactos congelados para análisis auditables. |

La plantilla usa `data/` y `outputs/` como separación explícita entre inputs y outputs. Esto es equivalente funcionalmente al principio `cin/`/`cout/` usado en otros proyectos del ecosistema, pero se conserva aquí porque la estructura MSE ya distingue además niveles de acceso, registros y certificación.

## Flujo científico recomendado

1. Definir el caso en `species_profile.yml`.
2. Definir objetivos y tolerancias de riesgo en `docs/01_governance_objectives/`.
3. Documentar el sistema biológico y pesquero.
4. Registrar evidencia, fuentes, datos y decisiones.
5. Definir alcance, horizonte temporal y complejidad del MSE.
6. Construir, condicionar y validar Operating Models.
7. Definir modelos de observación, estimación e implementación.
8. Definir Management Procedures candidatas.
9. Fijar métricas de desempeño antes de comparar alternativas.
10. Ejecutar simulaciones de ciclo cerrado.
11. Evaluar riesgo, desempeño y trade-offs.
12. Documentar circunstancias excepcionales, seguimiento y revisión.
13. Congelar una configuración auditable en `certification/` cuando corresponda.

## Datos, privacidad y publicación

La plantilla distingue `public`, `derived_public`, `internal` y `restricted`. `data/raw_private/` y `local_private/` están destinados a información que no debe entrar al historial Git.

`publication.yml` define reglas de exposición y `.gitignore` excluye credenciales, datos privados y outputs generados. Aun así, cada proyecto derivado debe revisar sus propias restricciones institucionales y de licencia antes de hacerse público.

## Reproducibilidad y validación

El repositorio incluye GitHub Actions para validar estructura, metadatos YAML y sintaxis Python. Esa validación comprueba la **infraestructura del template**; no certifica resultados científicos ni sustituye pruebas científicas de una MSE aplicada.

Los directorios `tests/unit`, `tests/integration`, `tests/regression` y `tests/scientific` son puntos de extensión para los proyectos generados. Deben poblarse con pruebas reales cuando exista código o comportamiento científico que validar.

## Metadatos e integración

- `template.yml` describe esta plantilla y declara el tipo de repositorio que produce por defecto.
- `repo.yml` describe **este repositorio template** para integración con GitHub Profile, web académica y automatización. Al generar un nuevo proyecto, ese archivo debe actualizarse inmediatamente.
- `CITATION.cff` contiene metadatos de citación del template.
- `VERSION` y `CHANGELOG.md` documentan su versión y evolución.

## Estado

**Versión:** `1.0.0`  
**Tipo:** `type-template`  
**Estado:** `active`  
**Etapa:** `stable`  
**Producto por defecto:** `type-project`  
**Idioma principal:** español

La versión `1.0.0` representa una estructura estable del template. No implica que un proyecto generado esté científicamente completo o certificado.

## Citación

Los metadatos de citación están definidos en [`CITATION.cff`](CITATION.cff). Si un proyecto derivado produce un artículo, reporte, dataset o software con una cita propia, ese output debe citarse de forma independiente y la metadata del repositorio derivado debe actualizarse.

## Licencias

El **código, scripts y componentes de software** se distribuyen bajo [MIT](LICENSE).

La **documentación, texto explicativo y figuras originales** se distribuyen bajo [CC BY 4.0](LICENSE-DOCS.md), salvo indicación expresa.

Los datos no quedan licenciados automáticamente por estas licencias. Cada dataset debe conservar y documentar sus propias condiciones de uso y redistribución.
