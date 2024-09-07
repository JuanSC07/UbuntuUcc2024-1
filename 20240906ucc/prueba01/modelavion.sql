/*==============================================================*/
/* DBMS name:      PostgreSQL 8                                 */
/* Created on:     06/09/2024 10:17:38 p. m.                    */
/*==============================================================*/


drop table AVION;

drop table CIUDAD;

drop table ITINEARIO;

/*==============================================================*/
/* Table: AVION                                                 */
/*==============================================================*/
create table AVION (
   ID                   DECIMAL(10)          not null,
   CAPACIDAD            NUMERIC(16,2)        null,
   COLOR                CHAR(20)             null,
   MARCA                CHAR(20)             null,
   MODELO               CHAR(20)             null,
   COLUMN_6             CHAR(10)             null,
   DAWDAWD              CHAR(10)             null,
   COLUMN_8             CHAR(10)             null,
   constraint PK_AVION primary key (ID)
);

/*==============================================================*/
/* Table: CIUDAD                                                */
/*==============================================================*/
create table CIUDAD (
   ID                   DECIMAL(20)          not null,
   NOMBRE               CHAR(20)             null,
   constraint PK_CIUDAD primary key (ID)
);

/*==============================================================*/
/* Table: ITINEARIO                                             */
/*==============================================================*/
create table ITINEARIO (
   ID                   DECIMAL(20)          not null,
   NOMBRE               CHAR(20)             not null,
   FECHASALIDA          DATE                 not null,
   HORASALIDA           TIME WITH TIME ZONE  null,
   AVIONID              DECIMAL(20)          not null,
   CIUDADIDSALIDA       DECIMAL(20)          not null,
   COLUMN_7             CHAR(10)             null,
   CIUDADIDLLEGADA      DECIMAL(20)          not null,
   COLUMN_9             CHAR(10)             null,
   constraint PK_ITINEARIO primary key (ID)
);

alter table ITINEARIO
   add constraint FK_ITINEARI_CIUDADREF_CIUDAD foreign key (CIUDADIDSALIDA)
      references CIUDAD (ID)
      on delete restrict on update restrict;

alter table ITINEARIO
   add constraint FK_ITINEARI_REFERENCE_AVION foreign key (AVIONID)
      references AVION (ID)
      on delete restrict on update restrict;

alter table ITINEARIO
   add constraint FK_ITINEARI_REFERENCE_CIUDAD foreign key (CIUDADIDLLEGADA)
      references CIUDAD (ID)
      on delete restrict on update restrict;

