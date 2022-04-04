Contribuir
========== 

If you don't speak Spanish you can check our [English version](CONTRIBUTING_en.md)

¡Todas las contribuciones son bienvenidas! Solo asegurate de que sigues las guías y tu cambio o mejora debería ser aceptada sin ningún problema

## Versión corta

* **Crea un tiquet en github** Si has encontrado un bug, quieres solicitar una mejora o quieres implementar una nueva funcionalidad. Asegurate que nadie ha creado un ticket (issue) similar!
* **Crea una pull request** y asegurate que tu commit contiene el número de issue. 

## Versión larga

### Paso 1: Crea un Issue

Antes de escribir código, asegúrate de que creas un issue que describa lo que te gustaría añadir o mejorar. De esa manera nos permite darte nuestra opinión antes de empezar, ya que puede que alguien ya esté trabajando en esa mejora, también es aconsejable sobre todo si es una contribución grande, darle un vistazo a nuestro canal en discord.

### Paso 2: Crea un Fork del Repository

Esto te permitirá añadir tus cambios en tu propio código base separado del nuestro.

### Paso 3: Añadir un Upstream Remoto

Para añadir un upstream remoto:

```bash
$ git remote add upstream git@github.com:JaimeObregon/subvenciones.git 
```

### Paso 4: Create un Feature Branch

Asegurate de darle a tu branch un nombre descriptivo que empieze con `feature` que incluya el número de issue,

e.g. `feature/123-add-contact-type`.

### Paso 5: Push a tu Fork

Cuando escribas código, asegúrate de hacer un push atomico a tu fork. También, asegúrate de incluir tu número de issue y la descripción del cambio en el mensaje del commit ej. `#123: Added a new Contact type` o `#234: Fixed a null pointer when loading single items from the API`.

Recuerda que diferentes issues van en branches separados!

### Paso 6: Rebase contra Upstream


Antes de crear tu pull request, has rebase de tu fork contra el upstream remoto para bajarte los ultimos cambios del repositorio, esto va a ayudar a minimizar los conflictos cuando se haga el merge:

```bash
$ git fetch upstream
$ git rebase upstream/develop
```

### Paso 7: Run Tests

Si tienes algun test, este es el momento de ejecutarlos


### Paso 8: Crear una Pull Request

Crea una pull request desde el feature branch (lo puedes hacer desde github), asegúrate de incluir una descripción de tus cambios. Debería haber un solo issue por pull request.
