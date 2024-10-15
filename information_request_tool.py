from datetime import datetime


INFO_DATA = {
  "reservation_contacts": {
    "France_individual_booking": {
      "contact": "00 820 835 835",
      "open_hours": {"Monday": (8, 22),
            "Tuesday": (8, 22),
            "Wednesday": (8, 22),
            "Thursday": (8, 22),
            "Friday": (8, 22),
            "Saturday": (8, 22),
            "Sunday": (9, 21),},
      "call_rate": "€0.12/min + call charges (Rate applicable from a landline in France, subject to change)."
    },
    "Antilles_Guyane_individual_booking": {
      "contact": "00 820 835 835",
      "open_hours": {
          "Monday": (8, 22),    # Opening hours from 7 a.m. to 7 p.m.
        "Tuesday": (8, 22),
        "Wednesday": (8, 22),
        "Thursday": (8, 22),
        "Friday": (8, 22),
        "Saturday": (8, 22),
        "Sunday": (9, 21)
            },     # Sunday and public holidays from 6 a.m. to 3 p.m.",
      "call_rate": "€0.11/min + call charges (Rate applicable from a landline in the French Antilles or French Guiana, subject to change)."
    },
    "France_preference_account_Student18_29": {
      "contact": "0 820 830 832",
      "open_hours":{
          "Monday": (8, 22),    # Opening hours from 7 a.m. to 7 p.m.
            "Tuesday": (8, 22),
            "Wednesday": (8, 22),
            "Thursday": (8, 22),
            "Friday": (8, 22),
            "Saturday": (8, 22),
            "Sunday": (9, 21)   # Sunday and public holidays from 6 a.m. to 3 p.m.
    },
      "call_rate": "€0.12/min + call charges (Rate applicable from a landline in Metropolitan France, subject to change)."
    },
    "Antilles_Guyane_preference_account_Student18_29": {
      "contact": "0 820 830 832",
      "open_hours":                
       { 
           "Monday": (7, 19),    # Opening hours from 7 a.m. to 7 p.m.
            "Tuesday": (7, 19),
            "Wednesday": (7, 19),
            "Thursday": (7, 19),
            "Friday": (7, 19),
            "Saturday": (7, 19),
            "Sunday": (7, 16)     # Sunday and public holidays from 7 a.m. to 4 p.m.
       },
      "call_rate": "€0.11/min + call charges (Rate applicable from a landline in French Antilles/Guyane, subject to change)."
    }
  },
  "cancellation_fee_invoice_request": {
    "electronic_ticket_invoice_information": "Important information: Your electronic ticket/travel memo received at the time of purchase serves as an invoice/receipt.",
    "requirements": "To obtain the requested document and claim reimbursement from your insurance for the portion not covered by Air Caraïbes, you must have canceled your booking by calling the call center and be in possession of a non-changeable, non-refundable ticket.",
    "call_center_contact": "0 820 835 835",
    "call_center_rate": "€0.12/min + call charges (Rate applicable from a landline in France, subject to change).",
    "email_request_address": "fraisannulation@aircaraibes.com",
    "email_instructions": "Include your booking number, full name, and details of the flight or service for which the fees were applied to facilitate quicker processing."
  },
  "group_booking_affreightment_contact": {
    "description": "Benefit from a group rate (starting from a minimum of 10 people traveling together).",
    "specific_charter_request": "Request a specific charter (aircraft rental) for official travel, business trips, etc.",
    "group_quotation_request": "For group rate quotes, please contact our customer service via the following form.",
    "contact_form_link": "https://www.aircaraibes.com/avant-voyage/tarifs-speciaux/groupes#no-back"
  },
  "refund_request": {
    "description": "To request a refund, select the reason for your request below.",
    "general_refund_request_link": "https://www.aircaraibes.com/gerer-reservation",
    "pass_zen_refund_request_link": "https://sav.cloud.aircaraibes.com/fr/formulaire-reclamation",
    "package_booking_information": "If you purchased a package or stay through a tour operator or your ticket from a travel agency, please contact your travel agency or tour operator. Reservations made through travel agencies are not eligible for refunds on our website."
  },
  "claim_request": {
    "description": "To file a claim, please click the link below to access our claims form.",
    "claim_form_link": "https://sav.cloud.aircaraibes.com/fr/formulaire-reclamation"
  }
}

FUNCT_DESCRIPTION = {
        "type": "function",
        "function": {
            "name": "information_request",
            "description": "A tool that provides specific contact information based on user queries. It is used to retrieve details like contact numbers, open hours, and call rates for various services.",
            "parameters": {
                "type": "object",
                "properties": {
                    "type_of_request": {
                        "type": "string",
                        "description": "The information requested based on the user query. e.g.: 'cancellation_fee_invoice_request'.",
                        "enum": [
                            "reservation_contacts - provides reservations information for services offered in both France and the French Antilles/Guyane, including contact numbers, open hours, and call rates for individual bookings and student preference accounts.",
                            "cancellation_fee_invoice_request - handles requests for cancellation fee invoices, guiding the user on using electronic tickets as receipts, cancellation procedures, and necessary contacts.",
                            "group_booking_affreightment_contact - offers information on group booking benefits for a minimum of 10 people traveling together, specific charter requests for official and business trips, and contact information for obtaining group rate quotes via an online form.",
                            "refund_request - provides information and links for requesting refunds, including details for general and Pass Zen refund requests and guidance for package bookings through travel agencies.",
                            "claim_request - gives access to filing a claim through a provided link to the claims form for handling complaints."
                        ]
                    },
                    "reservation_services": {
                        "type": "string",
                        "description": "What's the reservation services that the user has requested if the type_of_request is 'reservation_contacts'?, e.g. default service = 'France individual booking'",
                        "enum": [
                            "France individual booking",
                            "Antilles Guyane individual booking",
                            "France preference account for students aged between 18 - 29",
                            "Antilles Guyane preference account for students aged between 18 - 29"
                        ],
                        
                    },
                    "group_booking_affreightment_contact_request_type": {
                        "type": "string",
                        "description": "What's the request type for group booking affreighment that the user has choosen if the type_of_request is 'group_booking_affreightment_contact'?, e.g. default request type = 'specific charter request'",
                        "enum": [
                            "specific charter request",
                            "group quotation request"
                        ]
                    },
                    "refund_request_type": {
                        "type": "string",
                        "description": "What's the type of refund requested by the User if the choosen type_of_request is 'refund_request'?, default requested refund type = 'general refund request'",
                        "enum": [
                            "general refund request",
                            "pass zen refund request"
                        ]
                    },
                },
                "required": ["type_of_request"],
            },
        },
    }

class InformationRequestTool:
    params = {"run-method": "run", "tool-method": "run"}
    description = FUNCT_DESCRIPTION

    parameters = {
        "properties": {
            "main_form": {
                "type": "type_of_request",
                "label": "Information Requested",
                "description": "a list of main forms",
                "value":  "[\"Sub-form Before departure questions\",\"Sub-form Modification - only handles slight changes\",\"Sub-form Payment - Includes multiple charges\",\"Sub-form Cancellation - also handles deletions\",\"Sub-form Customer on spot\",\"Sub-form Claims\",\"Sub-form Member account\",\"sales - Information request on sales\"]"
            }
            
        }
    }

    configuration = {
        "id": "e_t1",
        "name": "information_request",
        "label": "INFORMATION REQUEST",
        "description": "Used to request information based on the type of User request",
        "category": "tool",
        "img": "assets/imgs/information-request-tool.jpg",
        "attach_node": {},
    }

    def __init__(self, config:dict, session=None, verbose=False):
        self.config = config # same as properties from parameters
        self.session = session # hold useful methods such as compact_llm, knowledge_base, etc
        self.verbose = verbose
        self.initialize()

    def initialize(self):
        """You can access some methods/instances from session
        1. ai:
            - compact_llms:
                * chat: to chat with llm based on specified configs, eg. {messages:list, tools:list, model:str, llm:str, temperature:float, is_json:bool, forced_tool:bool}
            - reranker: rerank documents based on configs eg. {question:str, documents:list, top:int}
        2. db:
            - get_kbid_by_name: get knowledge base IDs using their names, eg. **{names:list, envid:str}
            - get_urls_domains: return all urls of the given kbids, eg. **{kbids:list}
            - query_knowledgebase: query knowledge base for information, eg. **{queries:list, configs:dict}
        """
        # retrieve your properties from config below
        self.some_variable = self.config.get('some_name')
        # other logics below

    def run(self, **kwargs):
        
        # the parameters
        type_of_request = kwargs.get("type_of_request", "")
        reservation_services = kwargs.get("reservation_services", "")
        group_booking_affreightment_contact_request_type = kwargs.get("group_booking_affreightment_contact_request_type", "")
        refund_request_type = kwargs.get("refund_request_type", "")

        expected_response = None

        if type_of_request.startswith("reservation_contacts"):
            expected_response = self.handles_reservations_information(reservation_services)
        elif type_of_request.startswith("group_booking_affreightment_contact"):
            expected_response = self.handles_group_booking_affreightment_information(group_booking_affreightment_contact_request_type)
        elif type_of_request.startswith("cancellation_fee_invoice_request"):
            expected_response = self.handles_cancellation_fee_invoices()
        elif type_of_request.startswith("refund_request"):
            expected_response = self.handles_refund_information(refund_request_type)
        elif type_of_request.startswith("claim_request"):
            expected_response = self.handles_claim_information()
        # return statement
        if expected_response is not None:
            return {"status": "success", "response": expected_response, "token_count": 0,"cost": 0}
        else:
            return {"status": "fail", "response": "failed to retrieve information from the tool, please provide more details on how I can help you!", "token_count": 0,"cost": 0}
    
    def handles_reservations_information(self, reservation_services_p):
        if reservation_services_p.lower()=="France individual booking":
            service_name = INFO_DATA["reservation_contacts"]["France_individual_booking"]
            contact = service_name["contact"]
            call_rate = service_name["call_rate"]
            service_open_hours = service_name["open_hours"]
            if self.is_open(service_open_hours):
                return f"Please contact us on the following numbers: '{contact}'\nNote the call rates: {call_rate}"
            return "Please contact us next time during working during!"

        elif reservation_services_p.lower()=="Antilles Guyane individual booking":
            service_name = INFO_DATA["reservation_contacts"]["Antilles_Guyane_individual_booking"]
            contact = service_name["contact"]
            call_rate = service_name["call_rate"]
            service_open_hours = service_name["open_hours"]
            if self.is_open(service_open_hours):
                return f"Please contact us on the following numbers: '{contact}'\nNote the call rates: {call_rate}"
            return "Please contact us next time during working during!"
        
        elif reservation_services_p.lower()=="France preference account for students aged between 18 - 29":
            service_name = INFO_DATA["reservation_contacts"]["France_preference_account_Student18_29"]
            contact = service_name["contact"]
            call_rate = service_name["call_rate"]
            service_open_hours = service_name["open_hours"]
            if self.is_open(service_open_hours):
                return f"Please contact us on the following numbers: '{contact}'\nNote the call rates: {call_rate}"
            return "Please contact us next time during working during!"
        
        elif reservation_services_p.lower()=="Antilles Guyane preference account for students aged between 18 - 29":
            service_name = INFO_DATA["reservation_contacts"]["France_individual_booking"]
            contact = service_name["contact"]
            call_rate = service_name["call_rate"]
            service_open_hours = service_name["open_hours"]
            if self.is_open(service_open_hours):
                return f"Please contact us on the following numbers: '{contact}'\nNote the call rates: {call_rate}"
            return "Please contact us next time during working during!"
        else:
            return None

    def handles_cancellation_fee_invoices(self):
        electronic_ticket_invoice_information = INFO_DATA["cancellation_fee_invoice_request"]["electronic_ticket_invoice_information"]
        requirements = INFO_DATA["cancellation_fee_invoice_request"]["requirements"]
        call_center_contact = INFO_DATA["cancellation_fee_invoice_request"]["call_center_contact"]
        call_center_rate = INFO_DATA["cancellation_fee_invoice_request"]["call_center_rate"]
        email_request_address = INFO_DATA["cancellation_fee_invoice_request"]["email_request_address"]
        email_instructions = INFO_DATA["cancellation_fee_invoice_request"]["email_instructions"]
        
        return f"{electronic_ticket_invoice_information}\n{requirements}\nPlease contact the call center on the following numbers '{call_center_contact}', call rates: {call_center_rate}\nOr contact through email: '{email_request_address}'\n Please note:{email_instructions}"
        
    
    def handles_group_booking_affreightment_information(self, group_booking_affreightment_contact_request_type_p):
        
        if group_booking_affreightment_contact_request_type_p.lower() == "specific charter request":
            specific_charter_request = INFO_DATA["group_booking_affreightment_contact"]["specific_charter_request"].lower()[:-1]

            return f"Would you like to {specific_charter_request}?"
            
        elif group_booking_affreightment_contact_request_type_p.lower() == "group quotation request":
            group_booking_affreightment_contact = INFO_DATA["group_booking_affreightment_contact"]["description"]
            group_quotation_request = INFO_DATA["group_booking_affreightment_contact"]["group_quotation_request"]
            contact_form_link = INFO_DATA["group_booking_affreightment_contact"]["contact_form_link"]
            
            return f"{group_booking_affreightment_contact}\n{group_quotation_request}\n{contact_form_link}"
    
    def handles_refund_information(self, refund_request_type_p):
        print(refund_request_type_p)
        package_booking_information = INFO_DATA["refund_request"]["package_booking_information"]
        
        if refund_request_type_p.lower() == "general refund request":
            general_refund_request_link = INFO_DATA["refund_request"]["general_refund_request_link"]
            request_description = "Please click the following link to make your refund request:"
            return f"{request_description}\n{general_refund_request_link}\nPlease note:{package_booking_information}"
            
        elif refund_request_type_p.lower() == "pass zen refund request":
            pass_zen_refund_request_link = INFO_DATA["refund_request"]["pass_zen_refund_request_link"]
            request_description = "Please click the following link to make your refund request:"
            return f"{request_description}\n{pass_zen_refund_request_link}\nPlease note: {package_booking_information}"
        
        # elif refund_request_type_p == "":
            # return "Please provide me with correct type of your refund request"

    
    def handles_claim_information(self):
        claim_description = INFO_DATA["claim_request"]["description"]
        claim_form_link = INFO_DATA["claim_request"]["claim_form_link"]
        return f"{claim_description}\n{claim_form_link}"

    def is_open(self, open_hours):
        now = datetime.now()
        
        # Get the current day of the week and current hour
        current_day = now.strftime("%A")  # Full weekday name, e.g., "Monday"
        current_hour = now.hour           # Current hour in 24-hour format

        # Check if today is in the open hours dict
        if current_day in open_hours:
            opening_time, closing_time = open_hours[current_day]
            if opening_time <= current_hour < closing_time:
                return True
        
        return False
  