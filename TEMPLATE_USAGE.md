# Cómo usar este template para crear un MSE real

Este repositorio es una plantilla. Al utilizar **Use this template** en GitHub, el nuevo repositorio debe representar una especie, stock, pesquería o programa MSE concreto.

## Cambios mínimos al crear un proyecto

1. Actualice `repo.yml` inmediatamente: cambie `name`, `title`, `description`, `visibility`, `status`, `stage`, topics e integración. El tipo por defecto para una MSE aplicada es `type-project`.
2. Reemplace los campos de ejemplo en `species_profile.yml` por la información real del caso.
3. Revise `publication.yml` y la política institucional de datos antes de añadir material real.
4. Defina objetivos y tolerancias de riesgo antes de diseñar reglas de manejo.
5. Registre las fuentes disponibles en `registry/source_registry.csv` y los datos en `registry/data_inventory.csv`.
6. Documente el sistema real de manejo antes de reconstruir la Management Procedure de statu quo.
7. Mantenga como `TBD` cualquier elemento que todavía no tenga evidencia o una decisión científica formal.

## Clasificación del repositorio generado

La clasificación por defecto es `type-project`, porque una MSE aplicada representa normalmente un proyecto científico que puede producir varios outputs. No use múltiples `type-*` a la vez.

- Si el repositorio completo termina representando un único artículo, puede migrarse posteriormente a `type-paper` y renombrarse con sufijo `-paper`.
- Si el objetivo real es construir un pipeline reusable independiente de un caso aplicado, clasifíquelo como `type-workflow`.
- Papers, workflows, software y reportes derivados pueden vivir en repositorios separados y relacionarse mediante metadata en lugar de asignar varios tipos al mismo repo.

## Qué no debe copiarse ciegamente

El template **no prescribe** una escala temporal, estructura espacial, modelo de reclutamiento, mortalidad natural, crecimiento, relación ambiente-reclutamiento, modelo de evaluación, puntos de referencia ni HCR. Todos esos elementos deben definirse según el caso real.

El `repo.yml` heredado identifica a `.template-mse`; por tanto, también debe modificarse antes de integrar el nuevo proyecto con el GitHub Profile, la web académica o cualquier catálogo automatizado.

Consulte el [`README.md`](README.md) para la lógica general y [`REPOSITORY_MAP.md`](REPOSITORY_MAP.md) para navegar por las carpetas.
