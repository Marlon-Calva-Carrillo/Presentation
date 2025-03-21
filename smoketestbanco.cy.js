describe("Test suite - conjunto de pruebas", () =>{

         beforeEach(() => {
        // root-level hook
        // runs before every test block
        //Crear un before each para validar datos del usuario
        cy.visit("http://zero.webappsecurity.com/")
           })
        //Espacio de pruebas para validar la pagina en la que vamos a hacer pruebas
        it("validar pagina de inicio", ()=>{
            
            cy.get(".active > img").should("be.visible")  //Validamos que la imagen sea visible
            cy.get(".active >.custom > h4").contains("Online Banking")

        })

        it("Prueba E2E - Transferencia de fondos", ()=>{
        
            cy.get("#signin_button").click() //Click en el boton "Signin"
            cy.get("#user_login").type("username") //Ingresa el dato "username"
            cy.get("#user_password").type("password") //Ingresa el dato "password"
            cy.get(".btn").click() //Click en boton
            cy.get("#transfer_funds_tab > a").click()  //Click en boton "transfer_funds"
            cy.get("#tf_fromAccountId").select("1") //Seleccionamos el elemento 1 de las opciones
            cy.get("#tf_toAccountId").select("5") //Seleccionamos el elemento 5 de las opciones
            cy.get("#tf_amount").type("300")  //Escribe el valor 300
            cy.get("#tf_description").type("Transferencia de 300")  //Agregamos la descripcion del motivo de la transferencia
            cy.get("#btn_submit").click()  //Damos click en el boton llamado "submit"
            cy.get("#btn_submit").click()
            cy.get(".alert").contains("You successfully submitted your transaction.")  //Valida que muestre un mensaje favorecedor

        })
        //Espacio de pruebas para validar informacion de la grafica Insurance, Household, charity y restaurants
        it("Prueba de validacion de actualizacion del grafico", ()=>{
            
            cy.get("#signin_button").click()  //Selecciona el boton "signin"
            cy.get("#user_login").type("username")  //Escribe usuario
            cy.get("#user_password").type("password")  //Escribe contraseña
            cy.get(".btn").click()  //Click en boton
            cy.get("#money_map_tab > a").click() 
            cy.get("#ext-sprite-1259").should("be.visible")  //Valida graficos visibles
            cy.get("#ext-sprite-1167 > tspan").click()
            cy.get("#ext-sprite-1259").should("not.be.visible")

        })

})
