export interface Input {
  /**
   * New-listing identity returned by prepare-local-sourcebook-write. Evidence-bearing public fields are compiled by MCP Scraper and cannot be supplied here.
   */
  identity: {
    category: "home" | "professional" | "restaurants" | "financial" | "realestate" | "auto" | "wellness";
    state: string;
    businessName: string;
    websiteUrl: string;
    schemaOrgType?:
      | "LocalBusiness"
      | "AnimalShelter"
      | "AutomotiveBusiness"
      | "AutoBodyShop"
      | "AutoDealer"
      | "AutoPartsStore"
      | "AutoRental"
      | "AutoRepair"
      | "AutoWash"
      | "GasStation"
      | "MotorcycleDealer"
      | "MotorcycleRepair"
      | "ChildCare"
      | "Dentist"
      | "DryCleaningOrLaundry"
      | "EmergencyService"
      | "EmploymentAgency"
      | "EntertainmentBusiness"
      | "FinancialService"
      | "AccountingService"
      | "AutomatedTeller"
      | "BankOrCreditUnion"
      | "InsuranceAgency"
      | "FoodEstablishment"
      | "Bakery"
      | "BarOrPub"
      | "Brewery"
      | "CafeOrCoffeeShop"
      | "Distillery"
      | "FastFoodRestaurant"
      | "IceCreamShop"
      | "Restaurant"
      | "Winery"
      | "HealthAndBeautyBusiness"
      | "BeautySalon"
      | "DaySpa"
      | "HairSalon"
      | "HealthClub"
      | "NailSalon"
      | "TattooParlor"
      | "HomeAndConstructionBusiness"
      | "Electrician"
      | "GeneralContractor"
      | "HVACBusiness"
      | "HousePainter"
      | "Locksmith"
      | "MovingCompany"
      | "Plumber"
      | "RoofingContractor"
      | "LegalService"
      | "Library"
      | "LodgingBusiness"
      | "MedicalBusiness"
      | "Pharmacy"
      | "Physician"
      | "RealEstateAgent"
      | "RecyclingCenter"
      | "SelfStorage"
      | "ShoppingCenter"
      | "SportsActivityLocation"
      | "Store"
      | "TouristInformationCenter"
      | "TravelAgency";
    slug?: string;
    /**
     * @maxItems 20
     */
    tags?:
      | []
      | [string]
      | [string, string]
      | [string, string, string]
      | [string, string, string, string]
      | [string, string, string, string, string]
      | [string, string, string, string, string, string]
      | [string, string, string, string, string, string, string]
      | [string, string, string, string, string, string, string, string]
      | [string, string, string, string, string, string, string, string, string]
      | [string, string, string, string, string, string, string, string, string, string]
      | [string, string, string, string, string, string, string, string, string, string, string]
      | [string, string, string, string, string, string, string, string, string, string, string, string]
      | [string, string, string, string, string, string, string, string, string, string, string, string, string]
      | [string, string, string, string, string, string, string, string, string, string, string, string, string, string]
      | [
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string
        ]
      | [
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string
        ]
      | [
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string
        ]
      | [
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string
        ]
      | [
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string
        ]
      | [
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string
        ];
    idempotencyKey: string;
  };
  /**
   * @maxItems 20
   */
  tagCandidates?:
    | []
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ];
  /**
   * @maxItems 20
   */
  tagDecisions?:
    | []
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
          acceptCanonical?: string;
        }
      ];
}

export type Output = unknown
