<?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Obtén los datos del formulario
        $nombre = htmlspecialchars($_POST["nombre"]);
        $empresa = htmlspecialchars($_POST["empresa"]);
        $email = htmlspecialchars($_POST["email"]);
        $mensaje = htmlspecialchars($_POST["mensaje"]);

        // Configura los detalles del correo electrónico
        $destinatario = "denisarangue18@gmail.com";
        $asunto = "Contacto de la página web personal";
        $cuerpoMensaje = "Nombre: $nombre\nEmpresa: $empresa\nCorreo electrónico: $email\nMensaje:\n$mensaje";

        // Envía el correo electrónico
        if (mail($destinatario, $asunto, $cuerpoMensaje)) {
            // Muestra un mensaje de éxito
            echo "¡Gracias por contactarnos! Te responderemos lo antes posible.";
        } else {
            // Muestra un mensaje de error si no se pudo enviar el correo electrónico
            echo "Lo sentimos, ha ocurrido un error. Por favor, intenta nuevamente más tarde.";
        }
    }
?>
